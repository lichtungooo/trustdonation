---
name: td-quest
description: "Eine Quest für das Real Life Game bauen: gegliederte Beschreibung, Katalog-Tätigkeit, Wertung XP = 10 × h × (K + G + S + I), Aufteilung auf Bereiche und Lebens-Attribute, Bestätigung, Reihen. Für Eli, für den eigenen Agenten über MCP und für jeden, der mit einem Menschen eine Quest anlegt. Gleiche Tätigkeit ergibt überall dieselben XP."
---

# Eine Quest bauen

Timo am 03.10.2026: *"Eine Quest braucht eine ordentliche Beschreibung. Gut gegliedert, gute Bilder, Material, was die Leute mitbringen sollen, welches Level es braucht, oder es ist eine Einstiegsquest."*

Und: *"Wenn in Hamburg eine Quest ist, muss die genauso von Attributen her das hergeben wie in München."*

**Der wichtigste Satz vorweg:** Die KI wählt, der Code rechnet. Wer eine Quest baut, bestimmt die **Eingaben** (Tätigkeit, Stunden, Niveau, Rolle). Die XP-Zahl schreibt niemand von Hand und keine KI. Sie folgt aus der Regel, darum ist sie überall gleich.

---

## 0. Stand

| | |
|---|---|
| **Freigegeben** (Timo, 03.10.2026) | Wertung `regel_v1`, Kurve mit Exponent 1,6, Name „Zusammenarbeit“ im Macher-Paket, Seele wächst aus Schaffen, Musik und Kunst, Schenken, Stille und Ritual |
| **Im Code** (`packages/td-core/src/spiel.ts`) | noch die alte Fassung: feste Größen 10/25/50, Exponent 1,5, Deckel 500 XP, Rundungsfehler in `stufeAus` |
| **Folgt** | Umbau von `spiel.ts` nach Abschnitt 8 des Berichts, Tätigkeits-Katalog, MCP-Werkzeug `quest.verteile` |

Bis der Umbau steht, rechnet dieser Skill von Hand nach der Regel und schreibt den Rechenweg in die Quest. Er behauptet nie, dass eine Funktion existiert, die noch fehlt.

Grundlagen: `docs/REAL-LIFE-GAME-GRUNDMODELL.md` im Repo `rls-uebersicht` und die Recherche `10-vision/Real-Life-Network/Visionen/Module/07-Gamification-Recherche/08-ROLLENSPIEL-MATHEMATIK.md` im Workspace.

---

## 1. Was eine Quest ist

Eine Quest ist wie eine Veranstaltung: Ort auf der Karte, Datum, Uhrzeit. Sie wird über Antons Aktionsknopf (das Plus unten) angelegt, als weiterer Typ neben Veranstaltung und Ort. Dazu trägt sie, was ein Spiel braucht.

| Teil | Was darin steht | Pflicht |
|---|---|---|
| **Kopf** | Titel, Titelbild, ein Satz, worum es geht | ja |
| **Bilder** | Werk, Ort, Menschen | nein |
| **Ablauf** | Schritte, nummeriert, kein Fließtext | ja |
| **Material** | was mitzubringen ist, was vor Ort bereitliegt | wenn es etwas braucht |
| **Voraussetzung** | Einstiegsquest, oder Stufe X in Bereich Y, oder die vorige Quest der Reihe | ja |
| **Ort und Zeit** | Pin, Datum, Uhrzeit, Plätze | ja |
| **Gastgeber** | wer leitet und bestätigt | ja |
| **Tätigkeit** | ein Eintrag aus dem Katalog, mit Version | ja |
| **Wertung** | Stunden, Niveau, Rollen, daraus XP und Aufteilung | ja |
| **Lohn in der Realität** | Wissen, Werkzeug, Essen, Kontakt, Material | nein |
| **Bestätigung** | welche Wege gelten | ja |

**Zwei Handlungen für den Menschen:** Annehmen und Beobachten. Ablehnen gibt es keines.

**Einzelquest oder Reihe.** Beim Hochbeet heißt das: Rahmen bauen, füllen, bepflanzen. Die nächste Quest öffnet sich, wenn die vorige bestätigt ist. Wer die Reihe abschließt, bekommt ein Abzeichen und meist ein Item, keine Extra-XP.

---

## 2. Die Fragen stellen

In dieser Reihenfolge, so wie ein Mensch die Quest später liest:

1. **Was tut ihr?** In einem Satz, mit einem Verb. „Wir bauen ein Hochbeet aus Lärchenholz.“
2. **Für wen?** Einstieg für alle, oder braucht es Vorwissen? Ab welchem Alter?
3. **Wie lange wird wirklich getan?** Aktive Stunden, ohne Anreise und Pausen. Bei mehreren Tagen je Tag.
4. **Allein, mit anderen, oder leitet jemand an?**
5. **Was braucht man?** Material, Werkzeug, Kleidung.
6. **Wo und wann?**
7. **Was nimmt man mit nach Hause?** Das Werkstück, eine Ernte, einen Kontakt, Wissen.
8. **Wer bestätigt?**
9. **Gehört sie zu einer Reihe?**

**Was fehlt, bleibt leer.** Keine erfundene Stundenzahl, kein geschätztes Material. Fehlt die Dauer, wird die Quest nicht gewertet, bis sie da ist.

---

## 3. Die Tätigkeit wählen

Die Tätigkeit ist der Schlüssel für Hamburg = München. Sie steht in einem gemeinsamen, versionierten Katalog und trägt die festen Werte:

| Feld | Was | Beispiel Bogenschießen |
|---|---|---|
| `id@version` | Kennung | `bogenschiessen@1` |
| `compendium_code`, `met` | aus dem Compendium of Physical Activities 2024 | 15010, 4,3 |
| `stellvertreter` | wenn der Compendium keinen eigenen Code hat | (keiner) |
| `geist_zusatz` | +1, wenn schon der Einstieg Planen oder ein eigenes Werkstück verlangt | 0 |
| `innen`, `innen_ziel` | 0, 1 oder 2; Ziel Bewusstsein oder Seele | 1, Bewusstsein |
| `bereiche` | höchstens drei, Anteile in Zehnteln, Summe 1, Hauptanteil mindestens 0,5 | keiner im Macher-Paket |
| `stunden_richtwert` | je Format | Einsteigerkurs 2 |

**So wird gewählt:**

1. Gibt es die Tätigkeit schon als Alias? Dann diese nehmen, ohne weiter zu fragen.
2. Sonst die fünf ähnlichsten Einträge zeigen und genau einen wählen.
3. Passt keiner: einen neuen Eintrag **vorschlagen**, mit Compendium-Code oder Stellvertreter, Innen-Wert und Bereichsanteilen. Er hat den Status „vorgeschlagen“, bis ein Mensch ihn bestätigt.
4. Die Zuordnung als Alias speichern, damit die nächste gleiche Quest sie findet.

**Der Ort geht nie in die Wahl ein.** „Bogenschießen in Hamburg“ und „Bogenschießen in München“ treffen denselben Eintrag.

---

## 4. Die Wertung (`regel_v1`)

```
P  = h × (K + G + S + I)
XP = 10 × P
```

| Wert | Regel |
|---|---|
| `h` | aktive Stunden, je Tag höchstens 8, auf halbe Stunden abgerundet. Wer bestätigt, darf senken, nie heben |
| `K` Körper | MET der Tätigkeit: unter 3,0 → 1; 3,0 bis 5,9 → 2; ab 6,0 → 3 |
| `G` Geist | Niveau: Einsteiger 1, Fortgeschritten 2, Meister 3; plus `geist_zusatz` (höchstens 3); wer anleitet, mindestens 2 |
| `S` Sozial | allein 0; mit anderen (ab zwei bestätigten Menschen) 1; trägt die Gruppe (leitet an, richtet aus, dient) 2 |
| `I` Innen | aus dem Katalog: 0, 1 oder 2 |

**Größe als Anzeige:** bis 120 XP klein, bis 360 mittel, bis 1.080 groß, darüber episch. Die Größe ändert nichts an der Zahl.

**Nie in der Rechnung:** Ort, Datum, Wetter, Gruppengröße, Stufe der Person, Zahl der Zeugen.

### Beispiele, durchgerechnet

| Quest | h | K | G | S | I | XP | Größe |
|---|---|---|---|---|---|---|---|
| Bogenschießen-Einsteigerkurs, 2 h | 2 | 2 | 1 | 1 | 1 | **100** | klein |
| Hochbeet bauen, Wochenende, allein | 12 | 3 | 2 | 0 | 0 | **600** | groß |
| Kind das Löten beibringen, 1 h, der Mentor | 1 | 1 | 2 | 2 | 0 | **50** | klein |
| dieselbe Stunde, das Kind | 1 | 1 | 1 | 1 | 0 | **30** | klein |
| Schmiedekurs, 3 Tage | 21 | 3 | 2 | 1 | 0 | **1.260** | episch |
| Qigong-Gruppe, 1 h, jede Woche | 1 | 2 | 1 | 1 | 2 | **60** je Abend | klein |

Den Rechenweg schreibt die Quest in einer Zeile mit:
> 2 h × (Körper 2 + Geist 1 + Sozial 1 + Innen 1) = 10 Punkte → 100 XP · Körper 40, Geist 20, Soziales 20, Bewusstsein 20

---

## 5. Die Aufteilung

**Lebens-Universum** (für jede Quest, in jedem Spiel gleich):

| Lebens-Attribut | bekommt |
|---|---|
| Körper | 10 × h × K |
| Geist | 10 × h × G |
| Soziales | 10 × h × S, wenn S = 1 |
| Gemeinschaft | 10 × h × S, wenn S = 2 |
| Bewusstsein oder Seele | 10 × h × I, Ziel laut Katalog |

Die Summe ist immer die Quest-XP, ohne Rundung.

**Seele** wächst aus Schaffen mit den Händen, Musik und Kunst, anderen etwas schenken, Stille und Ritual (Timo, 03.10.2026). Solche Tätigkeiten tragen im Katalog `innen_ziel: seele`. Ein eigener Seelen-Katalog mit Seelenstufen folgt nach Recherche.

**Spiel-Universum** (etwa Macher): Die Bereichsanteile der Tätigkeit verteilen die XP auf Bereiche, Rundung nach größtem Rest. XP zählt im Bereich und in allen Oberbereichen. Attribute sind die Summe ihrer Wurzel-Bereiche. Wer anleitet, gibt die Hälfte der Bereichs-XP in „Lehren“, falls das Universum diesen Bereich führt.

**Namen:** Im Macher-Paket heißt der Bereich „Zusammenarbeit“. Kein Spielpaket trägt einen der sechs Lebens-Namen (Seele, Geist, Bewusstsein, Körper, Soziales, Gemeinschaft).

---

## 6. Bestätigung

| Weg | Wann |
|---|---|
| QR-Code vor Ort | Veranstaltung, Festival-Station, Werkstatt-Tag |
| Gastgeber | Standard, bestätigt am Ende |
| Mentor im Bereich | Schule, Werkstatt, mit Rolle oder höherer Stufe |
| Peer | andere Teilnehmer bestätigen sich gegenseitig (Mindestzahl offen) |
| Gruppe | eine Gruppe, die aus der Quest entsteht |
| Bild oder Video | zusätzlicher Beleg, nie allein |

Niemand bestätigt sich selbst. Die Bestätigung ist ein Tor und kein Faktor: Mehr Zeugen bringen keine Extra-XP.

---

## 7. Was eine Quest niemals trägt

- **Kein Feld `xp`, das ein Mensch oder eine KI setzt.** XP folgt aus den Eingaben
- **Keinen Ortsfaktor, keinen Event-Bonus, kein Doppel-XP-Wochenende.** Hamburg = München
- **Keinen Streak, keine Tageskappe mit Reset, keinen Verfall.** Keine Verlustangst
- **Keinen Abschlag für Erfahrene** bei einfachen Quests. Helfen lohnt sich immer
- **Keinen Bonus, der mit der Gruppengröße wächst.** Das Dorf zählt wie die Stadt
- **Keinen Zufall** bei XP oder beim Zugang zu Items
- **Keine Rangliste über Menschen.** Ranglisten ordnen nur Quests

---

## 8. Der Ablauf

### Mit einem Menschen

1. Die Fragen aus Abschnitt 2 stellen
2. Die Tätigkeit wählen (Abschnitt 3), neue Einträge als Vorschlag markieren
3. Die Wertung rechnen (Abschnitt 4), den Rechenweg zeigen
4. Die Beschreibung gegliedert schreiben: Kopf, Ablauf in Schritten, Material, Voraussetzung, Lohn
5. Den Bestätigungsweg festlegen
6. Bei einer Reihe: die Folgequests mit `vorausgesetzt` verknüpfen
7. Dem Menschen alles zeigen, er bestätigt oder ändert die Eingaben

### Über den eigenen Agenten (MCP)

Das Werkzeug `quest.verteile(titel, beschreibung, universum)` liefert Eingaben, nie XP:

```
{
  taetigkeit: "bogenschiessen@1" | { neu: Vorschlag },
  stunden: 2, tage: 1, niveau: "einsteiger",
  rollen: { teilnehmer: "mit-anderen", gastgeber: "traegt" },
  kandidaten: [...],
  begruendung: "Alias-Treffer"
}
```

Sprachmodelle antworten selbst bei Temperatur 0 nicht immer gleich. Darum entsteht Gleichheit aus dem Katalog und dem Alias-Speicher, nie aus dem Modell. Bei einem neuen Eintrag fragt das Werkzeug dreimal; sind die Antworten uneinig, entscheidet ein Mensch.

### Prüfen

Wenn der Umbau von `spiel.ts` steht, prüfen diese Tests (Skill `/td-test`):

- dieselbe Quest mit „Hamburg“ und mit „München“ ergibt dieselben Eingaben und dieselbe XP
- die Summe der Lebens-Anteile ist die Quest-XP
- `stufeVon(xpFuerStufe(n)) = n` für n = 1 bis 200
- Bereichsanteile summieren sich zu 1
- kein Paket-Name gleicht einem Lebens-Namen
- die Ausgabe von `quest.verteile` enthält kein Feld `xp`

---

## 9. Die Stufen

Kurve mit Exponent 1,6 (freigegeben 03.10.2026): `xpFuerStufe(n) = ceil(100 · (n−1)^1,6)`. Die Stufe ist das größte n mit `xpFuerStufe(n) ≤ xp`.

| Stufe | ab XP | aktive Stunden bei 50 XP je Stunde |
|---|---|---|
| 2 | 100 | 2 |
| 5 | 919 | 18 |
| 10 | 3.364 | 67 |
| 20 | 11.118 | 222 |
| 50 | 50.620 | 1.012 |

Eine Formel gilt für jede Achse: Gesamt, Bereich, Attribut, Lebens-Attribut. Die Gesamtstufe ist die Stufe der XP-Summe, nie die Summe von Stufen.

---

## Verwandt

- `docs/REAL-LIFE-GAME-GRUNDMODELL.md` (rls-uebersicht): das Grundmodell, Quest-Anatomie, Quest-Log, Items, Wischen
- `08-ROLLENSPIEL-MATHEMATIK.md` (Workspace, 07-Gamification-Recherche): die Herleitung jeder Zahl mit Quellen
- `packages/td-core/src/spiel.ts`: der Code, Umbau folgt
- Skill `/td-definieren`: bevor ein neues Feld der Quest entsteht
- Skill `/td-naht`: bevor die Quest in Antons Aktionsknopf kommt
- Skill `/td-test`: was geprüft wird
