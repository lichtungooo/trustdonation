# -*- coding: utf-8 -*-
"""Baut die Übersichtsseite des Baukastens.

Timo am 17.09.2026: *"Sehe ich denn überhaupt den Baukasten? Ich habe mal
geguckt. Ich finde den nirgends."*

Er hatte recht. Der Baukasten bestand aus JSON-Dateien, die man lesen, aber
nicht ansehen konnte. Diese Seite zeigt alle acht Schichten mit dem, was
drinsteht, und verlinkt jedes Stück, das sich öffnen lässt.

    python scripts/baukasten-seite-bauen.py

Schreibt `baukasten/index.html`. Die Daten sind **eingebettet**, nicht
nachgeladen: So lässt sich die Datei doppelklicken, ohne dass ein Server
läuft. Ein Browser verweigert `fetch` auf `file://`.

Die Datei wird **erzeugt**, nicht gepflegt. Die Quelle sind die JSON-Dateien.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BAU = REPO / "baukasten"

for strom in (sys.stdout, sys.stderr):
    try:
        strom.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

SCHICHTEN = [
    ("rohstoffe", "1", "Rohstoffe", "Farbe, Schrift, Maß. Was in allen drei Welten gleich ist.", [
        ("rohstoffe/farben.json", "farben"),
        ("rohstoffe/schriften.json", "schriften"),
        ("rohstoffe/masse.json", "masse"),
    ]),
    ("bauteile", "2", "Bauteile", "Die einzelnen Stücke. Je Welt eine Ausprägung, ein Aussehen.", [
        ("bauteile/bauteile.json", "bauteile"),
    ]),
    ("muster", "3", "Muster", "Zusammengesetzte Bauteile mit einer Absicht.", [
        ("muster/muster.json", "muster"),
    ]),
    ("felder", "4", "Felder", "Die kleinste Einheit, die ein Mensch ausfüllt.", [
        ("felder/felder.json", "felder"),
    ]),
    ("arten", "5", "Arten", "Eine Art bindet Felder und bestimmt, wie ein Eintrag aussieht.", [
        ("arten/arten.json", "arten"),
    ]),
    ("module", "6", "Module", "Die Flächen in der App.", [
        ("module/module.json", "module"),
    ]),
    ("vorlagen", "7", "Vorlagen", "Ganze Auftritte. Was eine Stiftung am meisten spart.", [
        ("vorlagen/vorlagen.json", "vorlagen"),
    ]),
    ("sprache", "8", "Sprache", "Die Worte. Die Schicht, die andere übersehen.", [
        ("sprache/sprache.json", "regeln"),
        ("sprache/sprache.json", "texte"),
    ]),
]


def sammle():
    """Liest alle Schichten und baut daraus eine Struktur für die Seite."""
    seite = []
    for kennung, nummer, titel, zweck, quellen in SCHICHTEN:
        eintraege = []
        fehlt = []
        gesehen = set()
        for pfad, schluessel in quellen:
            daten = json.loads((BAU / pfad).read_text(encoding="utf-8"))
            for e in daten.get(schluessel, []):
                eintraege.append({
                    "id": e.get("id", ""),
                    "name": e.get("name") or e.get("id", ""),
                    "zweck": e.get("zweck", ""),
                    "wert": e.get("wert"),
                    "datei": e.get("datei"),
                    "regel": e.get("regel") or e.get("absicht"),
                    "herkunft": (e.get("herkunft") or {}).get("name"),
                    "belege": e.get("belege") or [],
                })
            if pfad not in gesehen:
                fehlt.extend(daten.get("$fehlt", []))
                gesehen.add(pfad)
        seite.append({
            "id": kennung, "nummer": nummer, "titel": titel,
            "zweck": zweck, "eintraege": eintraege, "fehlt": fehlt,
        })
    return seite


VORLAGE = """<!doctype html>
<html lang="de">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Der Baukasten — trustdonation</title>
<link rel="stylesheet" href="rohstoffe/tokens.css">
<style>
  * { box-sizing:border-box; }
  body { margin:0; background:var(--weiss); color:var(--gruen);
         font:400 16px/1.6 var(--schrift-hanken); -webkit-font-smoothing:antialiased; }
  .mitte { max-width:1060px; margin:0 auto; padding:0 24px; }
  a { color:var(--rotbraun); }

  header { padding:56px 0 36px; background:var(--papier); border-bottom:1px solid var(--linie); }
  h1 { font-size:clamp(28px,4vw,40px); font-weight:800; letter-spacing:-.025em; margin:0 0 10px; }
  .einsatz { font-size:19px; color:var(--fliesstext); max-width:36em; margin:0 0 24px; }
  .summe { display:flex; flex-wrap:wrap; gap:26px; font-size:14.5px; }
  .summe b { font-size:23px; font-weight:800; display:block; line-height:1.2; }

  nav { position:sticky; top:0; z-index:5; background:var(--weiss);
        border-bottom:1px solid var(--linie); padding:12px 0; }
  nav .mitte { display:flex; flex-wrap:wrap; gap:7px; }
  nav a { display:inline-flex; align-items:center; gap:7px;
          border:1px solid var(--linie); border-radius:999px; padding:5px 13px;
          font-size:13.5px; font-weight:600; color:var(--gruen); text-decoration:none; }
  nav a:hover { background:var(--papier); }
  nav a i { font-style:normal; color:var(--gedaempft); font-size:12px; }

  section { padding:44px 0; border-top:1px solid var(--linie); }
  .kopf { display:flex; align-items:baseline; gap:12px; flex-wrap:wrap; margin-bottom:6px; }
  .nr { width:27px; height:27px; border-radius:50%; background:var(--gruen); color:var(--weiss);
        font-size:13px; font-weight:700; display:inline-flex; align-items:center;
        justify-content:center; flex:none; }
  h2 { font-size:25px; font-weight:800; letter-spacing:-.02em; margin:0; }
  .zaehler { font-size:13.5px; color:var(--gedaempft); }
  .zweck { color:var(--fliesstext); margin:0 0 22px; max-width:40em; }

  .gitter { display:grid; grid-template-columns:repeat(auto-fill,minmax(258px,1fr)); gap:14px; }
  .stueck { border:1px solid var(--linie); border-radius:var(--rundung);
            padding:15px 17px; background:var(--weiss); }
  .stueck .name { font-weight:700; font-size:15.5px; display:flex;
                  align-items:center; gap:9px; margin-bottom:5px; }
  .probe { width:17px; height:17px; border-radius:5px; flex:none;
           border:1px solid rgba(27,94,64,.18); }
  .stueck .text { font-size:14px; color:var(--fliesstext); }
  .stueck .regel { font-size:13px; color:var(--gedaempft); margin-top:9px;
                   padding-top:9px; border-top:1px solid var(--linie); }
  .stueck .fuss { font-size:12px; color:var(--gedaempft); margin-top:9px;
                  display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
  .stueck a.ansehen { font-size:12.5px; font-weight:600; }
  .beleg { background:var(--papier); border-radius:999px; padding:2px 9px; }

  .fehlt { margin-top:26px; border-left:3px solid var(--gold); padding:2px 0 2px 16px; }
  .fehlt h3 { font-size:12px; font-weight:700; text-transform:uppercase;
              letter-spacing:.13em; color:var(--gedaempft); margin:0 0 10px; }
  .fehlt ul { margin:0; padding:0; list-style:none; display:grid; gap:9px; }
  .fehlt li { font-size:14px; }
  .fehlt b { font-weight:600; }
  .fehlt span { color:var(--gedaempft); }

  footer { padding:36px 0 64px; font-size:13.5px; color:var(--gedaempft);
           border-top:1px solid var(--linie); }
  code { font-family:var(--schrift-system-monospace); font-size:.9em; }
</style>

<header>
  <div class="mitte">
    <h1>Der Baukasten</h1>
    <p class="einsatz">Woraus wir bauen. Was hier einmal entsteht, steht der Landingpage, der App und dem Web of Trust zur Verfügung.</p>
    <div class="summe">
      <span><b>__ANZAHL__</b>Bausteine</span>
      <span><b>8</b>Schichten</span>
      <span><b>__FEHLT__</b>benannte Lücken</span>
      <span><b>__STAND__</b>Stand</span>
    </div>
  </div>
</header>

<nav><div class="mitte">__NAV__</div></nav>

<div class="mitte">__ABSCHNITTE__</div>

<footer>
  <div class="mitte">
    Erzeugt aus <code>baukasten/*/*.json</code> durch <code>scripts/baukasten-seite-bauen.py</code>.
    Wer hier etwas ändern will, ändert die Quelle.<br>
    Die Festlegung steht in <a href="../docs/12-baukasten.md">docs/12-baukasten.md</a>,
    das Eintragsformat in <a href="EINTRAG.md">EINTRAG.md</a>.
  </div>
</footer>
"""


def html_schuetzen(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def main():
    schichten = sammle()
    anzahl = sum(len(s["eintraege"]) for s in schichten)
    fehlt_gesamt = sum(len(s["fehlt"]) for s in schichten)

    nav = "".join(
        f'<a href="#{s["id"]}">{html_schuetzen(s["titel"])} <i>{len(s["eintraege"])}</i></a>'
        for s in schichten
    )

    abschnitte = []
    for s in schichten:
        stuecke = []
        for e in s["eintraege"]:
            # Eine Farbe zeigt sich selbst. Ein Wort über eine Farbe ist
            # nutzlos, wenn man sie sehen kann.
            probe = ""
            if e["wert"] and str(e["wert"]).startswith("#"):
                probe = f'<span class="probe" style="background:{html_schuetzen(e["wert"])}"></span>'

            zeilen = [f'<div class="name">{probe}{html_schuetzen(e["name"])}</div>']
            text = e["zweck"] or ""
            if e["wert"] and not str(e["wert"]).startswith("#"):
                text = f'<code>{html_schuetzen(e["wert"])}</code> · {text}'
            elif e["wert"]:
                text = f'<code>{html_schuetzen(e["wert"])}</code> · {text}'
            if text:
                zeilen.append(f'<div class="text">{text}</div>')
            if e["regel"]:
                zeilen.append(f'<div class="regel">{html_schuetzen(e["regel"])}</div>')

            fuss = []
            if e["datei"] and e["datei"].endswith((".html", ".md")):
                ziel = e["datei"]
                if ziel.startswith("baukasten/"):
                    ziel = ziel[len("baukasten/"):]
                else:
                    ziel = "../" + ziel
                fuss.append(f'<a class="ansehen" href="{html_schuetzen(ziel)}">ansehen →</a>')
            for beleg in e["belege"][:2]:
                fuss.append(f'<span class="beleg">{html_schuetzen(beleg)}</span>')
            if fuss:
                zeilen.append('<div class="fuss">' + "".join(fuss) + "</div>")

            stuecke.append('<div class="stueck">' + "".join(zeilen) + "</div>")

        luecken = ""
        if s["fehlt"]:
            eintraege = "".join(
                f'<li><b>{html_schuetzen(f.get("name") or f.get("id", ""))}</b> '
                f'<span>{html_schuetzen(f.get("warum", ""))}</span></li>'
                for f in s["fehlt"]
            )
            luecken = (f'<div class="fehlt"><h3>Was hier noch fehlt</h3>'
                       f'<ul>{eintraege}</ul></div>')

        abschnitte.append(
            f'<section id="{s["id"]}">'
            f'<div class="kopf"><span class="nr">{s["nummer"]}</span>'
            f'<h2>{html_schuetzen(s["titel"])}</h2>'
            f'<span class="zaehler">{len(s["eintraege"])} steht, {len(s["fehlt"])} fehlt</span></div>'
            f'<p class="zweck">{html_schuetzen(s["zweck"])}</p>'
            f'<div class="gitter">{"".join(stuecke)}</div>'
            f'{luecken}</section>'
        )

    from datetime import date
    seite = (VORLAGE
             .replace("__ANZAHL__", str(anzahl))
             .replace("__FEHLT__", str(fehlt_gesamt))
             .replace("__STAND__", date.today().strftime("%d.%m."))
             .replace("__NAV__", nav)
             .replace("__ABSCHNITTE__", "".join(abschnitte)))

    ziel = BAU / "index.html"
    ziel.write_text(seite, encoding="utf-8", newline="\n")
    print(f"baukasten/index.html geschrieben: {anzahl} Bausteine in 8 Schichten, "
          f"{fehlt_gesamt} benannte Lücken")
    return 0


if __name__ == "__main__":
    sys.exit(main())
