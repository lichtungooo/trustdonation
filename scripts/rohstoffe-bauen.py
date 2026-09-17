# -*- coding: utf-8 -*-
"""Erzeugt die CSS-Variablen des Baukastens aus seiner Quelle.

Die Farben und Maße stehen in `baukasten/rohstoffe/*.json`. Damit ein
Bauteil sie benutzen kann, braucht es sie als CSS. Diese Datei erzeugt sie,
statt dass jemand sie abschreibt.

    python scripts/rohstoffe-bauen.py

Schreibt `baukasten/rohstoffe/tokens.css`. Die Datei wird **erzeugt**, nicht
gepflegt: Wer eine Farbe ändern will, ändert `farben.json`.

Nicht zu verwechseln mit `ds-bundle/tokens/tokens.css`. Das ist die
Gestaltung von **reallife.network**, ein anderes Projekt mit anderen Farben
(`--forest`, `--cream`, `--terracotta`).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROH = REPO / "baukasten" / "rohstoffe"

for strom in (sys.stdout, sys.stderr):
    try:
        strom.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    farben = json.loads((ROH / "farben.json").read_text(encoding="utf-8"))
    masse = json.loads((ROH / "masse.json").read_text(encoding="utf-8"))
    schriften = json.loads((ROH / "schriften.json").read_text(encoding="utf-8"))

    zeilen = [
        "/* Die Rohstoffe von trustdonation, als CSS-Variablen.",
        " *",
        " * ERZEUGT aus baukasten/rohstoffe/*.json durch scripts/rohstoffe-bauen.py.",
        " * Wer hier etwas ändert, verliert es beim nächsten Lauf. Die Quelle ist",
        " * farben.json.",
        " *",
        " * Jede Farbe steht zweimal: unter ihrem Namen im Baukasten und unter",
        " * jedem Namen, den sie auf der Seite trägt. So lassen sich Bauteile",
        " * schreiben, die beides verstehen.",
        " */",
        ":root {",
    ]

    for f in farben["farben"]:
        zeilen.append(f"  /* {f['zweck']} */")
        zeilen.append(f"  --{f['id']}: {f['wert']};")
        for name in f.get("seite", []):
            if name != f["id"]:
                zeilen.append(f"  --{name}: var(--{f['id']});")
        zeilen.append("")

    zeilen.append("  /* Maße */")
    for m in masse["masse"]:
        zeilen.append(f"  /* {m['zweck']} */")
        zeilen.append(f"  --{m['id']}: {m['wert']};")
        for name in m.get("seite", []):
            if name != m["id"]:
                zeilen.append(f"  --{name}: var(--{m['id']});")
    zeilen.append("")

    zeilen.append("  /* Schriften */")
    for s in schriften["schriften"]:
        zeilen.append(f"  /* {s['zweck']} */")
        familie = s["familie"]
        wert = f'"{familie}", system-ui, sans-serif' if s.get("datei") else familie
        zeilen.append(f"  --schrift-{s['id']}: {wert};")
    zeilen.append("}")
    zeilen.append("")

    # Die Fallen als Kommentar am Ende: Wer die Datei liest, soll sie sehen.
    if farben.get("$fallen"):
        zeilen.append("/* Achtung, zwei Namen meinen in der App etwas anderes:")
        for f in farben["$fallen"]:
            zeilen.append(f" *   {f['name']}: hier {f['seite']}, in der App {f['app']}")
        zeilen.append(" * Siehe baukasten/rohstoffe/farben.json, Abschnitt $fallen.")
        zeilen.append(" */")
        zeilen.append("")

    ziel = ROH / "tokens.css"
    ziel.write_text("\n".join(zeilen), encoding="utf-8", newline="\n")
    print(f"{ziel.relative_to(REPO).as_posix()} geschrieben: "
          f"{len(farben['farben'])} Farben, {len(masse['masse'])} Maße, "
          f"{len(schriften['schriften'])} Schriften")
    return 0


if __name__ == "__main__":
    sys.exit(main())
