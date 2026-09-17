---
name: td-stand
description: "Das Gedaechtnis von trustdonation pflegen und abrufen. Was am Anfang einer Runde gelesen wird, was am Ende geschrieben wird, wo welche Art von Wissen hingehoert, und wie eine neue Erfahrung nie wieder verlorengeht."
---

# Den Stand halten

Das Gedaechtnis ist kein Nebenprodukt. Es ist die Bedingung dafuer, dass eine neue Sitzung dort anfaengt, wo die letzte aufgehoert hat.

## Am Anfang einer Runde

In dieser Reihenfolge, immer:

```bash
cat /d/Workspace/memory/MEMORY.md                       # Block "WO STEHEN WIR"
cat /d/Workspace/memory/stand_trustdonation.md          # der Faden
cat /d/Workspace/memory/project_td_architektur.md       # wie wir bauen
cd /d/Workspace/20-repos/rls-uebersicht && python td-tools/anton-stand.py
```

Der letzte Befehl sagt, ob sich bei Anton etwas getan hat. Ohne ihn baut man auf einem Stand, der vielleicht schon veraltet ist.

Dazu, wenn es um Code geht:

| Datei | Was sie sagt |
|---|---|
| `docs/DEFINITION.md` | was wir bauen und nach welchen Mustern |
| `docs/ARCHITEKTUR.md` | wo es steht, welche Haken es gibt, wie Updates ankommen |
| `docs/NAEHTE.md` | wo wir Antons Code beruehren |
| `docs/PLAN.md` | was als Naechstes dran ist |

## Am Ende einer Runde

**Vor jeder Komprimierung und am Ende jeder Arbeitsrunde.** Vier Schritte:

### 1. Der Stand

`memory/stand_trustdonation.md`. Ein neuer Abschnitt oder ein aktualisierter, mit:

- **Was jetzt steht**: Image-Tag, Commit, was live ist.
- **Was unterwegs schiefging** und wie es geloest wurde. Das ist der wertvollste Teil.
- **Was als Naechstes dran ist.**
- Datum oben nachziehen.

Die Regel dafuer: **Ein Stolperstein, der eine Stunde gekostet hat, wird aufgeschrieben, damit er es nie wieder tut.**

### 2. Eine Erfahrung, wenn es eine gab

Drei Orte, je nach Art:

| Art | Wohin |
|---|---|
| **Wie Timo arbeitet**, eine Korrektur, eine bestaetigte Richtung | `memory/feedback_<thema>.md`, mit **Warum** und **How to apply** |
| **Ein Aussenverweis**, ein Verfahren, eine Adresse | `memory/reference_<thema>.md` |
| **Ein laufendes Vorhaben**, eine Entscheidung mit Wirkung | `memory/project_<thema>.md` |
| **Eine Runde mit Lehren fuer den ganzen Stack** | `40-forge/Real-Life-Forge/ERFAHRUNGEN.md`, als neue nummerierte Erfahrung |

Jede neue Datei bekommt **eine Zeile in `memory/MEMORY.md`**. Ohne die findet sie niemand wieder.

### 3. Was das Projekt beruehrt

- **Naehte gewachsen?** `docs/NAEHTE.md` nachziehen, Zahlen oben.
- **Eine Regel dazugekommen?** `docs/DEFINITION.md`.
- **Etwas ausgeliefert?** Image-Tag im Stand.
- **Eine Frist beruehrt?** `00-index/FRISTEN.md`.

### 4. Gegenprobe

```bash
cd /d/Workspace/20-repos/rls-uebersicht && python td-tools/anton-stand.py --ohne-fetch
```

Die Zeile **Unbenannt** muss `0` sein. Steht dort eine Zahl, fehlt ein Eintrag in `NAEHTE.md`, und die naechste Sitzung faellt darueber.

## Wo welches Wissen hingehoert

| Wissen | Ort | Warum dort |
|---|---|---|
| Wie etwas gebaut ist | `docs/` im Repo | wandert mit dem Code, ist versioniert |
| Wie wir arbeiten | Skills in `plugins/trustdonation-tools/skills/` | greift automatisch, wenn die Arbeit ansteht |
| Wo wir stehen | `memory/stand_*.md` | aendert sich staendig, gehoert nicht in den Code |
| Wer Timo ist und was er will | `memory/user_*.md`, `memory/feedback_*.md` | gilt ueber Projekte hinweg |
| Was einmal schiefging | Stand **und** Skill | im Stand als Geschichte, im Skill als Warnung an der richtigen Stelle |

**Die letzte Zeile ist die wichtigste.** Eine Falle nur im Stand zu notieren hilft niemandem, der sie gerade auslaeuft. Sie gehoert zusaetzlich in den Skill, der bei dieser Arbeit greift. Die Seed-Version steht darum an drei Stellen: im Stand, in `feedback_seed_version.md` und in den Skills `td-update` und `td-ausliefern`.

## Die Skills aktuell halten

Quelle ist das Repo `lichtungooo/trustdonation`:

```bash
cd /d/Workspace/20-repos/trustdonation
git pull
python scripts/skills-spiegeln.py --pruefen     # was weicht ab
python scripts/skills-spiegeln.py               # uebernehmen
```

Die Richtung ist eine Einbahn: **Aenderungen entstehen im Repo**, damit sie versioniert sind und alle sie bekommen. Ein lokal geaenderter Skill wird beim Spiegeln ueberschrieben.

## Was nicht ins Gedaechtnis gehoert

- Was das Repo schon sagt (Struktur, Git-Geschichte, vergangene Fehlerbehebungen).
- Was nur fuer diese eine Sitzung gilt.
- Eine Zusammenfassung dessen, was ohnehin in `docs/` steht. Lieber verweisen.

## Verwandt

- `CLAUDE.md` im Workspace, Abschnitt "STAND pflegen"
- `memory/stand_trustdonation.md`, `memory/project_td_architektur.md`
- Skills `td-anton`, `td-naht`
