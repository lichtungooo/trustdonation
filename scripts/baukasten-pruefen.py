# -*- coding: utf-8 -*-
"""Prüft den Baukasten: acht Schichten, ein Eintragsformat, keine toten Verweise.

Ein Baukasten, den niemand prüft, zerfällt still: Eine Datei wird umbenannt,
ein Bauteil verweist ins Leere, ein Feld steht zweimal da. Das fällt erst auf,
wenn jemand danach greift.

    python scripts/baukasten-pruefen.py

Geprüft wird:

  1. Jede Schicht-Datei ist gültiges JSON und da.
  2. Jeder Eintrag trägt id, name/zweck, herkunft und belege (siehe EINTRAG.md).
  3. Jede `datei` zeigt auf etwas, das existiert.
  4. Ids sind ASCII und eindeutig.
  5. Verweise zwischen Schichten gehen ins Volle: ein Bauteil, das einen
     Rohstoff nennt, nennt einen, den es gibt.

Rückgabe 0, wenn alles trägt. 1, wenn etwas fehlt.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BAU = REPO / "baukasten"

for strom in (sys.stdout, sys.stderr):
    try:
        strom.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Welche Datei trägt welche Liste. Die Reihenfolge ist die der Schichten:
# Rohstoffe zuerst, Sprache zuletzt.
SCHICHTEN = [
    ("1 Rohstoffe: Farben", "rohstoffe/farben.json", "farben"),
    ("1 Rohstoffe: Schriften", "rohstoffe/schriften.json", "schriften"),
    ("1 Rohstoffe: Maße", "rohstoffe/masse.json", "masse"),
    ("2 Bauteile", "bauteile/bauteile.json", "bauteile"),
    ("3 Muster", "muster/muster.json", "muster"),
    ("4 Felder", "felder/felder.json", "felder"),
    ("5 Arten", "arten/arten.json", "arten"),
    ("6 Module", "module/module.json", "module"),
    ("7 Vorlagen", "vorlagen/vorlagen.json", "vorlagen"),
    ("8 Sprache", "sprache/sprache.json", "regeln"),
]

# Rohstoffe und Felder tragen keine Herkunft: Eine Farbe gehört niemandem.
OHNE_HERKUNFT = {"farben", "schriften", "masse"}

# Ids bleiben ASCII. Kebab-case fuer Bausteine, camelCase fuer Felder: Die
# werden im Code als Eigenschaften gelesen (`data.summeVon`).
ASCII_ID = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9-]*$")


def lade(pfad):
    p = BAU / pfad
    if not p.exists():
        return None, f"fehlt: baukasten/{pfad}"
    try:
        return json.loads(p.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as fehler:
        return None, f"kaputt: baukasten/{pfad} ({fehler})"


def main():
    funde = []
    ohne_zweck = []
    zahlen = []
    alle_ids = {}

    for titel, pfad, schluessel in SCHICHTEN:
        daten, fehler = lade(pfad)
        if fehler:
            funde.append(fehler)
            zahlen.append((titel, 0, 0))
            continue

        eintraege = daten.get(schluessel, [])
        fehlt = daten.get("$fehlt", [])
        zahlen.append((titel, len(eintraege), len(fehlt)))

        for e in eintraege:
            kennung = e.get("id", "(ohne id)")
            wo = f"{pfad} → {kennung}"

            if not ASCII_ID.match(str(kennung)):
                funde.append(f"{wo}: Id ist keine ASCII-Kennung (kleingeschrieben, Bindestriche)")

            doppelt = alle_ids.setdefault(schluessel, {})
            if kennung in doppelt:
                funde.append(f"{wo}: Id steht in dieser Schicht zweimal")
            doppelt[kennung] = True

            if not e.get("zweck") and not e.get("name"):
                ohne_zweck.append(wo)

            if schluessel not in OHNE_HERKUNFT:
                if "herkunft" not in e:
                    funde.append(f"{wo}: keine Herkunft (siehe EINTRAG.md)")
                if "belege" not in e:
                    funde.append(f"{wo}: keine Belege (eine leere Liste ist eine gültige Antwort)")

            datei = e.get("datei")
            if datei and not (REPO / datei).exists():
                funde.append(f"{wo}: verweist auf `{datei}`, das es nicht gibt")

    # Verweise zwischen den Schichten
    farben, _ = lade("rohstoffe/farben.json")
    masse, _ = lade("rohstoffe/masse.json")
    bauteile, _ = lade("bauteile/bauteile.json")
    muster, _ = lade("muster/muster.json")

    if farben and masse and bauteile:
        bekannt = {f["id"] for f in farben["farben"]} | {m["id"] for m in masse["masse"]}
        for b in bauteile["bauteile"]:
            for r in b.get("rohstoffe", []):
                if r not in bekannt:
                    funde.append(f"bauteile → {b['id']}: nennt den Rohstoff `{r}`, den es nicht gibt")

    if bauteile and muster:
        bekannt = {b["id"] for b in bauteile["bauteile"]}
        for m in muster["muster"]:
            for b in m.get("bauteile", []):
                if b not in bekannt:
                    funde.append(f"muster → {m['id']}: nennt das Bauteil `{b}`, das es nicht gibt")

    # Der Bericht
    print("Der Baukasten von trustdonation")
    print()
    print(f"{'Schicht':26} {'steht':>6} {'fehlt':>6}")
    print("-" * 40)
    gesamt_da = gesamt_offen = 0
    for titel, da, offen in zahlen:
        gesamt_da += da
        gesamt_offen += offen
        print(f"{titel:26} {da:>6} {offen:>6}")
    print("-" * 40)
    print(f"{'zusammen':26} {gesamt_da:>6} {gesamt_offen:>6}")
    print()

    if ohne_zweck:
        print(f"{len(ohne_zweck)} Einträge haben keinen Zweck. Sie stehen da, ohne zu sagen wofür:")
        for z in ohne_zweck[:8]:
            print("  " + z)
        if len(ohne_zweck) > 8:
            print(f"  ... und {len(ohne_zweck) - 8} weitere")
        print()

    if funde:
        print(f"{len(funde)} Stellen tragen nicht:")
        for f in funde:
            print("  " + f)
        return 1

    print(f"{gesamt_da} Einträge, {gesamt_offen} benannte Lücken, {len(ohne_zweck)} ohne Zweck.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
