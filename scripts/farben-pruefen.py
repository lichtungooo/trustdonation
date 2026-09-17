# -*- coding: utf-8 -*-
"""Prüft, ob Seite und App dieselben Farben tragen.

Die Farben von trustdonation stehen an drei Orten:

    baukasten/rohstoffe/farben.json   die eine Quelle
    landing/site.css                  was die Landingpage benutzt
    branding/theme.json               was die App benutzt

Solange niemand nachsieht, laufen sie auseinander: Jemand ändert ein Grün
auf der Seite, und die App bleibt beim alten. Es fällt erst auf, wenn zwei
Bilder nebeneinander liegen.

Dieses Werkzeug vergleicht alle drei. Es ändert nichts, es sagt nur, was
nicht mehr zusammenpasst.

    python scripts/farben-pruefen.py

Rückgabe 0, wenn alles stimmt. 1, wenn etwas auseinanderläuft.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

for strom in (sys.stdout, sys.stderr):
    try:
        strom.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def farben_der_seite():
    """Die CSS-Variablen aus dem hellen Schema.

    Der erste Treffer je Name gewinnt: Das Dunkel-Schema steht weiter unten
    und überschreibt dieselben Namen.
    """
    text = (REPO / "landing" / "site.css").read_text(encoding="utf-8")
    gefunden = {}
    for treffer in re.finditer(r"--([a-z0-9-]+):\s*([^;]+);", text):
        name, wert = treffer.group(1), treffer.group(2).strip()
        if name not in gefunden:
            gefunden[name] = wert
    return gefunden


def farben_der_app():
    daten = json.loads((REPO / "branding" / "theme.json").read_text(encoding="utf-8"))
    return daten.get("light", daten)


def quelle():
    pfad = REPO / "baukasten" / "rohstoffe" / "farben.json"
    return json.loads(pfad.read_text(encoding="utf-8"))


def pruefe():
    q = quelle()
    seite = farben_der_seite()
    app = farben_der_app()
    funde = []

    bekannt_seite = set()
    bekannt_app = set()

    for farbe in q["farben"]:
        soll = farbe["wert"].upper()
        for name in farbe["seite"]:
            bekannt_seite.add(name)
            ist = seite.get(name)
            if ist is None:
                funde.append(f"Seite kennt `--{name}` nicht mehr (erwartet {soll} für „{farbe['id']}“)")
            elif ist.startswith("#") and ist.upper() != soll:
                funde.append(f"Seite: `--{name}` ist {ist.upper()}, die Quelle sagt {soll} („{farbe['id']}“)")
        for name in farbe["app"]:
            bekannt_app.add(name)
            ist = app.get(name)
            if ist is None:
                funde.append(f"App kennt `{name}` nicht mehr (erwartet {soll} für „{farbe['id']}“)")
            elif isinstance(ist, str) and ist.startswith("#") and ist.upper() != soll:
                funde.append(f"App: `{name}` ist {ist.upper()}, die Quelle sagt {soll} („{farbe['id']}“)")

    # Was neu dazugekommen ist, ohne in der Quelle zu stehen. Eine neue Farbe
    # ist keine Katastrophe, nur ein Hinweis: Sie gehört eingetragen, sonst
    # weiß beim nächsten Mal niemand, wofür sie da war.
    for name, wert in seite.items():
        if name not in bekannt_seite and wert.startswith("#"):
            funde.append(f"Seite führt `--{name}` = {wert.upper()}, das in der Quelle fehlt")
    for name, wert in app.items():
        if name not in bekannt_app and isinstance(wert, str) and wert.startswith("#"):
            funde.append(f"App führt `{name}` = {wert.upper()}, das in der Quelle fehlt")

    return funde, q


def main():
    funde, q = pruefe()

    fallen = q.get("$fallen", [])
    if fallen:
        print("Namen, die in beiden Welten vorkommen und Verschiedenes meinen:")
        for f in fallen:
            print(f"  `{f['name']}`  Seite {f['seite']}  |  App {f['app']}")
        print()

    if funde:
        print(f"{len(funde)} Stellen laufen auseinander:")
        for f in funde:
            print("  " + f)
        print()
        print("Zum Richten: die Quelle `baukasten/rohstoffe/farben.json` und die")
        print("beiden Dateien in Einklang bringen. Die Quelle gewinnt.")
        return 1

    print(f"{len(q['farben'])} Farben, an allen drei Orten gleich. Sauber.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
