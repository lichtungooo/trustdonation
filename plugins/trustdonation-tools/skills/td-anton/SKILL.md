---
name: td-anton
description: "Wo steht Anton, was hat er released, und was heisst das fuer uns. Erzeugt einen Bericht mit td-tools/anton-stand.py, liest ihn (Kollisionen, neue Erweiterungspunkte, Spec-Aenderungen, Releases) und entscheidet, ob jetzt aktualisiert wird. Regelmaessig laufen lassen."
---

# Antons Stand ansehen

Die Schnittstelle zu Antons Arbeit. Sie beantwortet vier Fragen, bevor irgendetwas angefasst wird.

**Wann:** regelmaessig, mindestens vor jeder Arbeitsrunde am Prototyp, und immer bevor `td-update` laeuft.

## Der Bericht

```bash
cd /d/Workspace/20-repos/rls-uebersicht
python td-tools/anton-stand.py
```

Das Werkzeug **liest nur**. Es aendert nichts am Arbeitsstand. Es holt `origin/master` samt Tags, vergleicht und schreibt nach `td-tools/berichte/anton-<datum>.md`.

Weitere Aufrufe:

```bash
python td-tools/anton-stand.py --ohne-fetch          # ohne Netz
python td-tools/anton-stand.py --basis <sha>         # gegen einen anderen Stand
```

## Die Kurzfassung lesen

```text
Basis        f9c56fff      worauf unser Branch aufsetzt
Sein Stand   f9c56fff      wo sein master steht
Neu bei ihm  0 Commits     wieviel dazugekommen ist
Unsere Naehte 27 Dateien   wo wir seinen Code beruehren
Kollisionen  0             wieviele davon er angefasst hat
Unbenannt    0             Naehte ohne Eintrag in NAEHTE.md
Neue Haken   0             Commits an seinen Erweiterungspunkten
Neue Tags    0             was er veroeffentlicht hat
```

**Die drei Zahlen, auf die es ankommt:**

| Zahl | Bedeutung |
|---|---|
| **Kollisionen** | So viele Konflikte sind beim Zusammenfuehren zu erwarten. Null heisst: laeuft durch. |
| **Unbenannt** | Groesser als null heisst **anhalten**: Wir aendern Code von Anton, ohne es eingetragen zu haben. Erst eintragen (Skill `td-naht`), dann weiter. |
| **Neue Haken** | Groesser als null heisst: Er hat vielleicht gebaut, was eine unserer Naehte aufloest. Der billigste Moment, sie loszuwerden. |

## Den Bericht lesen

Er ist nach Dringlichkeit geordnet:

1. **Urteil** zuerst, in zwei Saetzen: wieviel kommt, was trifft uns.
2. **Was er getan hat**: Commits mit Datum und Titel.
3. **Was unsere Naehte trifft**: je Datei unser Umfang und die Zahl seiner Commits darauf.
4. **Abgleich mit dem Register**: was in `docs/NAEHTE.md` fehlt.
5. **Neue Erweiterungspunkte**: Commits an seinen Registern, oder deren Titel nach einem Haken klingt.
6. **Spec-Aenderungen**: **Die Spec gewinnt.** Diese Dateien lesen und `docs/DEFINITION.md` danach pruefen.
7. **Releases**: Tags, Versionssprünge, neue Abhaengigkeiten.
8. **Naechster Schritt**: was konkret zu tun ist.

## Entscheiden

| Lage | Entscheidung |
|---|---|
| Keine neuen Commits | Nichts tun. Die Naehte kosten nichts, solange er ruht. |
| Neue Commits, null Kollisionen | Aktualisieren, wenn Zeit ist. `td-update` laeuft glatt durch. |
| Kollisionen an Naehten mit niedrigem Risiko | Aktualisieren. Konflikte sind bekannt und in `NAEHTE.md` beschrieben. |
| Kollision an A1 oder A2 (hohes Risiko) | Erst den Bericht genau lesen. Hat er den Dialog oder den Umschalter umgebaut, ist das eine eigene Sitzung. |
| Neue Erweiterungspunkte gemeldet | **Zuerst** pruefen, ob eine Naht wegfallen kann. Danach aktualisieren. Das spart mehr, als es kostet. |
| Spec-Aenderungen gemeldet | Lesen, bevor gebaut wird. Unsere Definition wird berichtigt, nie seine Spec. |
| Unbenannte Naehte gemeldet | Anhalten, eintragen, dann weiter. |

## Wenn er einen Haken gebaut hat

Das ist der wertvollste Fall, und er wird leicht uebersehen.

1. Den gemeldeten Commit ansehen: `git show <sha>`.
2. Fragen: **Loest das eine unserer Naehte?** Besonders A1 (Bereiche im Space-Dialog) und A2 (Gliederung im Umschalter) warten auf genau so etwas.
3. Wenn ja: Die Naht wird zu einer Erweiterung. Das ist ein eigener Schritt, mit Test, und `NAEHTE.md` verliert einen Eintrag.
4. Wenn nein: im Bericht vermerken, warum nicht. Beim naechsten Mal muss niemand dieselbe Pruefung wiederholen.

## Was das Werkzeug nicht sieht

- **Was er vorhat.** Offene Pull Requests und Issues stehen nicht im Bericht. Bei einem grossen Sprung lohnt ein Blick auf `github.com/real-life-org/real-life-stack/pulls`.
- **Warum er etwas geaendert hat.** Die Commit-Titel sagen das *was*. Bei einer Kollision an einer Naht mit hohem Risiko: `git show <sha>` lesen, bevor der Konflikt geloest wird.
- **Ob ein Release schon als Image vorliegt.** Tags im Repo und Bilder auf `ghcr.io` sind zwei Dinge.

## Danach

- Aktualisieren: Skill `td-update`.
- Etwas von uns zu ihm bringen: Skill `td-beitragen`.
- Bericht bleibt in `td-tools/berichte/` liegen. Die Reihe ist die Geschichte unserer Kopplung und wird nicht aufgeraeumt.

## Verwandt

- `docs/ARCHITEKTUR.md` Teil 2 (die Haken) und Teil 5 (der Update-Ablauf)
- `docs/NAEHTE.md`
- Skills `td-update`, `td-naht`, `td-beitragen`
