# Der Baukasten

Woraus wir bauen. Was hier einmal entsteht, steht der Landingpage, der App und dem Web of Trust zur Verfügung.

Die Festlegung steht in [docs/12-baukasten.md](../docs/12-baukasten.md). **Kein Marktplatz:** Ein Baustein ist Werkzeug, ein Angebot ist ein Anliegen.

---

## Die acht Schichten

| Schicht | steht | benannte Lücken | Datei |
|---|---:|---:|---|
| **1. Rohstoffe: Farben** | 13 | 0 | `rohstoffe/farben.json` |
| **1. Rohstoffe: Schriften** | 2 | 0 | `rohstoffe/schriften.json` |
| **1. Rohstoffe: Maße** | 3 | 0 | `rohstoffe/masse.json` |
| **2. Bauteile** | 3 | 4 | `bauteile/bauteile.json` |
| **3. Muster** | 2 | 4 | `muster/muster.json` |
| **4. Felder** | 43 | 0 | `felder/felder.json` |
| **5. Arten** | 5 | 3 | `arten/arten.json` |
| **6. Module** | 8 | 0 | `module/module.json` |
| **7. Vorlagen** | 3 | 4 | `vorlagen/vorlagen.json` |
| **8. Sprache** | 4 + 11 Werkzeuge | 5 | `sprache/sprache.json` |
| **zusammen** | **86** | **20** | |

Jeder Eintrag folgt [EINTRAG.md](EINTRAG.md): id, name, zweck, herkunft, belege, abstand.

**Die zwanzig Lücken sind Absicht.** Sie stehen als `$fehlt` in den Dateien, mit dem Grund, warum sie zählen. Ein Baukasten, der nur zeigt, was da ist, verschweigt die Hälfte.

## Die Prüfung

```bash
python scripts/baukasten-pruefen.py
```

Prüft alle acht Schichten: gültiges JSON, vollständige Einträge, keine toten Dateiverweise, eindeutige Ids, und ob ein Bauteil nur Rohstoffe nennt, die es gibt.

```bash
python scripts/farben-pruefen.py
```

Vergleicht die Farben mit `landing/site.css` und `branding/theme.json`.

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

Die zwanzig Lücken stehen in den Dateien. Nach Nutzen geordnet:

1. **Die fünf Textbausteine** (Erstansprache, Einladung, Absage, Nachfassen, Dankeschön). Sie kosten am wenigsten und sparen am meisten: Die meisten scheitern nicht an der Technik, sondern an der Frage, was sie schreiben sollen.
2. **Die vier fehlenden Bauteile** (Eingabefeld, Avatar, Kartennadel, Vertrauens-Anzeiger). Ohne sie hat jede Fläche ihr eigenes Aussehen.
3. **Die vier Vorlagen** (Landingpage einer Stiftung, Space „Stiftung", „Projekt", „Netzwerk"). Das ist es, was eine Stiftung am Ende wirklich will.
4. **Die drei fehlenden Arten** (Verein, Unternehmen, Mensch).
5. **Die vier Muster** (Profilkopf, Projektvorstellung, Kontaktblock, Förderaufruf).

## Zwei Entscheidungen, die anstehen

**Die Schriften.** `bricolage.woff2` (40 KB) und `spectral-italic.woff2` (14 KB) werden ausgeliefert und nie geladen. Entweder einsetzen, wie das `ds-bundle` es beschreibt, oder entfernen. Beides ist besser als heute.

**Die Rundungen.** Acht verschiedene Werte (8, 9, 10, 12, 14, 18, 50%, 999px), fünf davon als feste Zahl im Stil statt als Variable. Ein Vorschlag steht in `rohstoffe/masse.json`: drei Stufen plus Pille und Kreis. Das ist Arbeit an der Seite, kein reines Aufräumen, also erst mit Sebastian besprechen.
