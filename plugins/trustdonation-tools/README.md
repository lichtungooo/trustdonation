# trustdonation-tools

Elf Skills für die Arbeit an trustdonation. Sie tragen, was wir beim Bauen gelernt haben, an genau der Stelle, an der es gebraucht wird.

## Die Skills

| Skill | Wann |
|---|---|
| `td-stand` | **Am Anfang jeder Runde.** Was lesen, was am Ende schreiben |
| `td-anton` | Wo steht Anton, was hat er veröffentlicht, was heißt das für uns |
| `td-definieren` | **Bevor eine Sache Code wird.** Das Raster, Antons sechs Muster |
| `td-naht` | **Bevor Code von Anton geändert wird.** Haken prüfen, Eingriff klein ziehen |
| `td-modul` | Ein Space-Modul bauen, über das Register statt in seinen Code |
| `td-komponente` | Eine Oberflächen-Komponente bauen, nachdem gesucht wurde, ob es sie gibt |
| `td-test` | Was getestet wird: jede Liste, jede Regel aus der Definition |
| `td-performance` | Messen statt raten, mit den echten Zahlen von heute |
| `td-update` | Antons Stand einspielen, neun Schritte, drei Tore |
| `td-beitragen` | Etwas von uns zu ihm zurückbringen, Anwendungsfall zuerst |
| `td-ausliefern` | Bauen und auf trustdonation.org bringen |

## Benutzen

Dieses Repo ist die Quelle. Nach jedem `git pull`:

```bash
python scripts/skills-spiegeln.py --pruefen    # was weicht ab
python scripts/skills-spiegeln.py              # übernehmen
```

Die Richtung ist eine Einbahn: **Änderungen entstehen hier im Repo**, damit sie versioniert sind und alle sie bekommen.

Alternativ als Plugin einbinden, dann greift die Datei `.claude-plugin/marketplace.json` im Wurzelverzeichnis.

## Grundlagen

Die Skills verweisen auf vier Dokumente im Prototyp-Branch `trustdonation` von `lichtungooo/real-life-stack`:

| Datei | Inhalt |
|---|---|
| `docs/DEFINITION.md` | was wir bauen und nach welchen Mustern |
| `docs/ARCHITEKTUR.md` | wo es steht, welche Haken es gibt, wie Updates ankommen |
| `docs/NAEHTE.md` | jede Stelle, an der wir Antons Code berühren |
| `docs/PLAN.md` | in welcher Reihenfolge |
| `docs/REIFE.md` | was zur vollen Professionalität noch fehlt |

Dazu zwei Werkzeuge in `td-tools/`: `anton-stand.py` (die Schnittstelle zu Antons Arbeit) und `pruefen.py` (alle Tore in einem Befehl).
