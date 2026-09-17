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
| **2. Bauteile** | 7 | 2 | `bauteile/bauteile.json` |
| **3. Muster** | 2 | 4 | `muster/muster.json` |
| **4. Felder** | 43 | 0 | `felder/felder.json` |
| **5. Arten** | 5 | 3 | `arten/arten.json` |
| **6. Module** | 8 | 0 | `module/module.json` |
| **7. Vorlagen** | 7 | 2 | `vorlagen/vorlagen.json` |
| **8. Sprache: Regeln** | 4 + 11 Werkzeuge | 3 | `sprache/sprache.json` |
| **8. Sprache: Texte** | 5 | 0 | `sprache/texte/` |
| **zusammen** | **99** | **14** | |

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

## Schicht 2: Die Bauteile

`bauteile/stuecke/` führt die vier, die trustdonation wirklich braucht. Jedes ist eine Seite, die man im Browser öffnet:

| Bauteil | Die Regel darin |
|---|---|
| [Eingabefeld](bauteile/stuecke/feld.html) | Die Beschriftung steht über dem Feld, nicht darin. Der Fehler sagt, was dadurch nicht geht, statt „Pflichtfeld" |
| [Avatar](bauteile/stuecke/avatar.html) | Rund für Menschen, gerundet für Einrichtungen. Ein Punkt statt eines Hakens |
| [Kartennadel](bauteile/stuecke/kartennadel.html) | Ein Tropfen, kein Kreis. Die Farbe kommt von der Art, nicht vom Thema |
| [Vertrauens-Anzeiger](bauteile/stuecke/vertrauens-anzeiger.html) | Menschen statt Punkte. **Niemals eine Zahl, die man erhöhen kann** |

Sie benutzen `rohstoffe/tokens.css`, das aus der Quelle erzeugt wird:

```bash
python scripts/rohstoffe-bauen.py
```

**Nicht zu verwechseln mit `ds-bundle/`.** Das ist die Gestaltung von reallife.network, ein anderes Projekt mit anderen Farben (`--forest`, `--cream`, `--terracotta`). Die drei Bauteile, die dort liegen, belegen jenes Projekt, nicht unseres.

---

## Schicht 7: Die Vorlagen

Ein fertiger Auftritt, statt Knöpfe auszusuchen. Vier stehen:

| Vorlage | Was sie mitbringt |
|---|---|
| [Space Stiftung](vorlagen/spaces/stiftung.json) | vier Module, Art `stiftung`, Farbe der Art. Nach dem Vorbild Löwenherz |
| [Space Projekt](vorlagen/spaces/projekt.json) | dasselbe für ein Vorhaben. Kann zugleich ein eigenes Netzwerk sein |
| [Space Netzwerk](vorlagen/spaces/netzwerk.json) | `isNetwork` macht alles auf: Arten-Editor, Landingpage-Bereich, erster Platz im Umschalter |
| [Landingpage einer Stiftung](vorlagen/landingpage-stiftung.html) | eine fertige Seite, alles daraus aus den Feldern |

**Die drei Space-Vorlagen folgen der echten Struktur**, nicht einer erdachten: Sie sind aus deinen eigenen Spaces abgelesen. Jede erklärt in `$erklaerung`, warum ein Feld dasteht, und was passiert, wenn es fehlt.

Zwei Beispiele daraus:

- *Eine Stiftung ist Mitglied eines Netzwerks, kein eigenes.* Wer `isNetwork` setzt, bekommt den Arten-Editor und den Landingpage-Bereich, und beides braucht sie nicht.
- *Eine Art ohne `labelPlural` gilt als unvollständig und wird nicht gespeichert.* Das ist `zeileVollstaendig` in td-core.

**Die Landingpage stellt fünf Zahlen vor jeden Text.** Ein Projekt sucht zuerst eine Antwort: Passe ich überhaupt? Fördersumme, Reichweite, Antragsweg, Fristen, Eigenmittel. Erst danach kommen Sätze.

---

## Schicht 8: Die Texte

`sprache/texte/` führt die Bausteine, die eine Stiftung am Tisch braucht:

| Baustein | Wann | Der Kern |
|---|---|---|
| [Erstansprache](../docs/07-ansprache.md) | vor dem ersten Kontakt | steht im Zusammenhang der drei Türen und bleibt dort |
| [Nachfassen](sprache/texte/nachfassen.md) | nach zwei bis drei Wochen | ein Ausweg, der leicht fällt. Und kein drittes Mal |
| [Einladung](sprache/texte/einladung.md) | jemand soll mitarbeiten | die Verifizierung wird erklärt, nicht vorausgesetzt |
| [Absage](sprache/texte/absage.md) | eine Förderung wird abgelehnt | der Grund zeigt auf ein Kriterium, nicht auf Qualität |
| [Dankeschön](sprache/texte/dankeschoen.md) | nach einer Zusage | der Dank in einem Satz, danach was folgt |

**Jeder Text sagt auch, was wegbleibt.** Das ist der nützlichere Teil: „Leider müssen wir Ihnen mitteilen" sagt nichts, und „wir sind überwältigt" macht die nächste Bitte schwerer.

---

## Was als Nächstes dran ist

Die zwanzig Lücken stehen in den Dateien. Nach Nutzen geordnet:

1. **Die vier Muster** (Profilkopf, Projektvorstellung, Kontaktblock, Förderaufruf). Sie sitzen zwischen dem, was steht: Bauteile gibt es, Vorlagen auch, aber nichts dazwischen.
2. **Die drei fehlenden Arten** (Verein, Unternehmen, Mensch).
3. **Die Landingpage eines Projekts**, mit den anderen Zahlen: Bedürfnis, Bedarf, Lücke, Wirkung.

## Zwei Entscheidungen, die anstehen

**Die Schriften.** `bricolage.woff2` (40 KB) und `spectral-italic.woff2` (14 KB) werden ausgeliefert und nie geladen. Entweder einsetzen, wie das `ds-bundle` es beschreibt, oder entfernen. Beides ist besser als heute.

**Die Rundungen.** Acht verschiedene Werte (8, 9, 10, 12, 14, 18, 50%, 999px), fünf davon als feste Zahl im Stil statt als Variable. Ein Vorschlag steht in `rohstoffe/masse.json`: drei Stufen plus Pille und Kreis. Das ist Arbeit an der Seite, kein reines Aufräumen, also erst mit Sebastian besprechen.
