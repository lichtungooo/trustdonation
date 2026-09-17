# Was jeder Eintrag trägt

Jeder Baustein, gleich welcher Schicht, beantwortet dieselben sechs Fragen. Ohne sie ist der Baukasten eine Kiste, in der man wühlt.

| Feld | Frage | Pflicht |
|---|---|---|
| `id` | Wie heißt er, in ASCII, ohne Leerzeichen? | ja |
| `name` | Wie heißt er für Menschen? | ja |
| `zweck` | Wofür ist er da, in Sätzen? | ja |
| `herkunft` | Wer hat ihn gebaut? | ja |
| `belege` | Wo läuft er? | ja |
| `abstand` | Wie weit hat sich eine Übernahme entfernt? | bei Übernahmen |

---

## herkunft

**Wer ihn gebaut hat, als Relation auf ein Profil im Web of Trust**, nicht als Textfeld.

```json
"herkunft": { "did": "did:key:z6Mk...", "name": "Timo" }
```

Solange es noch keine Profile gibt, genügt der Name. Sobald es sie gibt, wird daraus eine Relation, und jeder Baustein trägt seine Vertrauenskette mit: Wer ihn übernimmt, sieht, von wem er kommt, und entscheidet selbst.

**Kein Textfeld**, weil ein Text sich nicht prüfen lässt. „Von Anton" schreibt jeder hin.

---

## belege

**Wo er schon läuft.** Eine Liste von Adressen oder Space-Ids.

```json
"belege": ["trustdonation.org", "lichtung.ooo"]
```

Das ist wertvoller als jede Bewertung und folgt dem zweiten Grundsatz: **Fakten statt Noten.** Ein Baustein, der an drei Orten trägt, braucht keine Sterne.

Eine leere Liste ist eine ehrliche Antwort: Er ist gebaut, aber noch nirgends im Einsatz.

---

## abstand

**Wie weit eine Übernahme sich vom Original entfernt hat.** Nur bei Bausteinen, die von einem anderen abstammen.

```json
"abstand": { "von": "muster/hero", "geaendert": ["farben", "reihenfolge"], "stand": "2026-09-17" }
```

Ohne das laufen zwanzig Stiftungsseiten auseinander, und niemand merkt es, bis die Marke zerfällt. Mit dem Abstand sieht jeder: Diese Seite folgt dem Muster, jene hat sich weit entfernt, **und das kann gute Gründe haben.**

Der Abstand ist kein Vorwurf. Er ist eine Auskunft.

---

## Was ausdrücklich fehlt

**Keine Bewertung, keine Rangliste, keine Empfehlung von oben.** Wer einen Baustein sucht, sieht drei Dinge: was er tut, wer ihn gebaut hat, wo er läuft. Daraus entscheidet er selbst.

**Keine Downloadzahlen.** Sie messen Neugier, nicht Tauglichkeit.

---

## Sonderfelder je Schicht

Über die sechs gemeinsamen hinaus trägt jede Schicht, was sie braucht:

| Schicht | zusätzlich |
|---|---|
| Rohstoffe | `wert`, und die Namen in beiden Welten (`seite`, `app`) |
| Bauteile | `datei`, `welt` (seite / app / beide) |
| Muster | `bauteile` (woraus es besteht), `absicht` |
| Felder | `shape`, `multiple`, `label`, `input` (siehe DEFINITION Teil 7) |
| Arten | `felder` (welche es bindet), `farbe`, `fragebogen` |
| Module | `moduleId`, `art` (daten / code), `presents`, `itemTypes` |
| Vorlagen | `schichten` (was sie zusammensetzt) |
| Sprache | `wann` (in welcher Lage), `laenge` |
