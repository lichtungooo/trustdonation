# Der Baukasten

Woraus wir bauen. Was hier einmal entsteht, steht der Landingpage, der App und dem Web of Trust zur Verfügung.

Die Festlegung steht in [docs/12-baukasten.md](../docs/12-baukasten.md). **Kein Marktplatz:** Ein Baustein ist Werkzeug, ein Angebot ist ein Anliegen.

---

## Die acht Schichten und wo sie stehen

| Schicht | Stand | Wo |
|---|---|---|
| **1. Rohstoffe** | **steht, geprüft** | `rohstoffe/farben.json` |
| 2. Bauteile | teilweise | `../ds-bundle/components/` (Band, Knöpfe, Karten) |
| 3. Muster | teilweise | `../ds-bundle/patterns/` (Hero, Einladung) |
| 4. Felder | definiert | `DEFINITION.md` Teil 7 im Stack-Repo |
| 5. Arten | definiert, Editor gebaut | `DEFINITION.md` Teil 6, `packages/td-ui` |
| 6. Module | Antons sieben stehen | eigene fehlen |
| 7. Vorlagen | Fragebögen stehen | [../docs/fragen/](../docs/fragen/) |
| 8. Sprache | steht | fünfzehn Skills in `../plugins/` |

---

## Schicht 1: Die Farben

`rohstoffe/farben.json` führt **jede Farbe genau einmal**, mit beiden Namen, die sie trägt.

Denn sie wird an zwei Orten gebraucht, und dort heißt sie verschieden:

| Bedeutung | auf der Seite | in der App |
|---|---|---|
| Grün | `--gruen` | `primary` |
| Linie | `--line` | `border` |
| Gedämpft | `--muted` | `muted-foreground` |

### Zwei Wörter, die lügen

| Wort | auf der Seite | in der App |
|---|---|---|
| `muted` | `#6B8578`, eine **Schriftfarbe** | `#FFF8F1`, eine **helle Fläche** |
| `accent` | `#B5390A`, dunkles Rotbraun | `#FFE4CC`, helles Pfirsich |

Dasselbe Wort meint in beiden Welten Gegensätzliches. Wer zwischen ihnen wechselt, greift daneben. Beides steht als `$fallen` in der Datei, damit es niemanden mehr überrascht.

### Die Prüfung

```bash
python scripts/farben-pruefen.py
```

Vergleicht alle drei Orte: die Quelle, `landing/site.css` und `branding/theme.json`. Es ändert nichts, es sagt nur, was nicht mehr zusammenpasst.

Stand 17.09.2026: **13 Farben, an allen drei Orten gleich.**

---

## Was als Nächstes dran ist

1. **Die Bauteile aus `ds-bundle` hierher**, mit Herkunft und Belegen. Heute liegen sie in einem Bündel, das für `reallife.network` erzeugt wurde, nicht für trustdonation.
2. **Schriften und Maße** als zweite Rohstoff-Datei, nach demselben Muster wie die Farben.
3. **Die drei Zusatzfelder** für jeden Eintrag: Herkunft (als Relation auf ein Profil), Belege (wo er läuft), Abstand (wie weit eine Übernahme sich entfernt hat).

**Nicht alles bauen.** Erst das Vorhandene an einen Ort räumen. Ein Baukasten mit acht halben Schichten an vier Orten hilft niemandem.
