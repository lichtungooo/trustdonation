# Der Baukasten

**Status:** Normativer Entwurf

Timo am 17.09.2026: *"Ich habe die ganze Zeit den Marktplatz im Kopf. Einen Ort, wo wir Module bauen können, wo die Module drin sind, wo wir allerdings auch für die Landingpage gewisse Bausteine bauen können, wo wir Komponenten bauen können."*

Der Baukasten ist der Ort, aus dem gebaut wird. Was einmal entsteht, steht danach allen zur Verfügung: der Landingpage, der App und dem Web of Trust.

---

## Der Name ist eine Festlegung

| Wort | Wofür es steht |
|---|---|
| **Baukasten** | woraus wir bauen. Werkzeug |
| **Marktplatz** | wo Menschen einander Angebot und Bedarf zeigen. Anliegen |

Ein Baustein ist Werkzeug. Ein Angebot ist ein Anliegen. Wer beides gleich nennt, verwechselt sie später im Code und in den Daten.

Der Marktplatz bekommt eine eigene Definition, wenn er dran ist.

---

## Warum es drei Welten und acht Schichten braucht

Unsere drei Welten tragen verschiedene Materialien:

| Welt | Material |
|---|---|
| Landingpage | HTML und CSS |
| Die App | React |
| Web of Trust | Daten, als Items |

**Ein Knopf kann darum nicht in allen dreien dasselbe Stück sein.** Wer das versucht, baut eine Schicht, die überall halb passt.

Was in allen dreien dasselbe sein **kann**, liegt eine Ebene tiefer: Farbe, Schrift, Abstand, Rundung. Darauf steht die Schichtung.

---

## Die acht Schichten

### 1. Rohstoffe

Farben, Schriften, Abstände, Rundungen, hell und dunkel.

**Steht, mit Prüfung** (seit 17.09.2026): `baukasten/rohstoffe/farben.json` führt jede Farbe **genau einmal**, und `scripts/farben-pruefen.py` hält sie mit den beiden Orten in Einklang, an denen sie gebraucht wird.

Denn sie standen vorher zweimal da, unter verschiedenen Namen:

| Bedeutung | `landing/site.css` | `branding/theme.json` |
|---|---|---|
| Grün | `--gruen` | `primary` |
| Linie | `--line` | `border` |

Beim ersten Vergleich stimmten alle dreizehn Farben überein. **Zwei Wörter meinten allerdings Gegensätzliches:** `muted` ist auf der Seite eine Schriftfarbe (`#6B8578`), in der App eine helle Fläche (`#FFF8F1`). Bei `accent` dasselbe. Beides steht jetzt als Falle in der Quelle.

`ds-bundle/tokens/tokens.css` bleibt daneben bestehen: Es ist eine **Ableitung** für den Design-Agenten, erzeugt aus denselben zwei Dateien, keine eigene Quelle.

Diese Schicht ist die wichtigste, weil sie als einzige wirklich überall gilt. Solange sie stimmt, sehen drei verschiedene Welten gleich aus.

### 2. Bauteile

Knopf, Karte, Band, Feld, Etikett, Avatar, Kartennadel, Vertrauens-Anzeiger.

**Teilweise da:** `ds-bundle/components/` führt Band, Knöpfe und Karten als HTML. Die App hat ihre eigenen in Antons Toolkit.

**Die Regel:** Ein Bauteil hat je Welt eine Ausprägung und **ein** Aussehen. Wer den Knopf der Landingpage ändert, ändert die Rohstoffe, nicht den Knopf der App.

### 3. Muster

Hero, Einladung, Kontaktblock, Profilkopf, Projektvorstellung, Spendenaufruf.

**Teilweise da:** `ds-bundle/patterns/` führt Hero und Einladung.

Ein Muster ist mehr als die Summe seiner Bauteile: Es trägt eine Absicht. „Hero" heißt: Das Erste, was jemand sieht, und es muss in drei Sekunden sagen, worum es geht.

### 4. Felder

Förderrahmen, Antragsfrist, Anschrift, Schwerpunkt, Rechtsform, Gemeinnützigkeit.

Ein Feld ist die kleinste Einheit, die ein Mensch ausfüllt. Es kennt seine Form (Text, Zahl, Datum, Auswahl, Ort), seine Sichtbarkeit und seine Frage.

Die Definition steht in `DEFINITION.md` Teil 7 (Stack-Repo), das Datenmodell in [03-datenmodell.md](03-datenmodell.md).

### 5. Arten

Stiftung, Projekt, Verein, Netzwerk, Unternehmen, Mensch.

Eine Art bindet Felder: Eine Stiftung trägt andere Angaben als ein Projekt. Sie bestimmt auch, wie ein Eintrag aussieht, welche Farbe seine Kartennadel hat und welche Fragen gestellt werden.

Definition in `DEFINITION.md` Teil 6.

### 6. Module

Die Flächen in der App: Karte, Liste, Board, Kalender, Feed, Graph.

Dazu eigene, die es noch nicht gibt:

| Modul | Was es täte |
|---|---|
| **Förderfinder** | zeigt einem Projekt, welche Stiftungen zu ihm passen, mit Gründen |
| **Antragshelfer** | führt durch einen Antrag, Frage für Frage, und merkt sich Antworten für den nächsten |
| **Wirkungsbericht** | was aus einer Förderung wurde, in Fakten statt Prosa |
| **Spendenverlauf** | wer wann wohin gab, sichtbar für die Beteiligten |
| **Förderkalender** | Antragsfristen als Termine, damit keine verpasst wird |

**Die Grenze:** Im Real Life Stack entsteht ein Modul durch Programmieren, Bauen und Ausliefern. *"Ein Space ist KEINE Schicht, das Register steht vor dem ersten Render fest."* Wer ein Modul ohne Code bauen will, baut es im Real Life Network.

Definition in `DEFINITION.md` Teil 8.

### 7. Vorlagen

Ganze Auftritte, aus den Schichten darunter zusammengesetzt:

- Eine fertige Landingpage für eine Stiftung
- Ein Space „Stiftung", ein Space „Projekt", ein Space „Netzwerk"
- Die Fragebögen aus [fragen/](fragen/)

Eine Vorlage ist das, was eine Stiftung am meisten spart. Sie will keine Knöpfe aussuchen, sie will einen Auftritt haben.

### 8. Sprache

Die fünfzehn Skills, dazu Textbausteine: Erstansprache, Einladung, Absage, Nachfassen, Dankeschön.

**Die Schicht, die andere übersehen.** Ein Baukasten, der auch die Worte mitliefert, spart einer Stiftung mehr Zeit als jeder Knopf. Die meisten scheitern nicht an der Technik, sondern an der Frage, was sie schreiben sollen.

---

## Was jeder Eintrag zusätzlich trägt

Drei Felder, die aus einer Sammlung einen Baukasten machen:

### Herkunft

Wer es gebaut hat, als **Relation auf ein Profil** im Web of Trust, nicht als Textfeld.

Dann trägt jeder Baustein seine Vertrauenskette mit. Wer ihn übernimmt, sieht, von wem er kommt, und kann selbst entscheiden.

### Belege

Wo er schon läuft. *"Dieses Muster steht auf trustdonation.org und auf lichtung.ooo."*

Das ist wertvoller als jede Bewertung und folgt Grundsatz 2: **Fakten statt Noten.** Ein Baustein, der an drei Orten trägt, braucht keine Sterne.

### Abstand

Wie weit eine Übernahme sich vom Original entfernt hat.

Ohne das laufen zwanzig Stiftungsseiten auseinander, und niemand merkt es, bis die Marke zerfällt. Mit dem Abstand sieht jeder: Diese Seite folgt dem Muster, jene hat sich weit entfernt, und das kann gute Gründe haben.

---

## Was der Baukasten nicht ist

Kein Laden. Keine Bezahlung. Keine Bewertungen. Keine Rangliste. Keine Empfehlung von oben.

Wer einen Baustein sucht, sieht drei Dinge: **was er tut, wer ihn gebaut hat, wo er läuft.** Daraus entscheidet er selbst.

---

## Wo es heute steht

| Schicht | Stand | Wo |
|---|---|---|
| Rohstoffe | **steht, geprüft** | `baukasten/rohstoffe/farben.json` plus `scripts/farben-pruefen.py` |
| Bauteile | teilweise | `ds-bundle/components/` (Band, Knöpfe, Karten) |
| Muster | teilweise | `ds-bundle/patterns/` (Hero, Einladung) |
| Felder | definiert | `DEFINITION.md` Teil 7, [03-datenmodell.md](03-datenmodell.md) |
| Arten | definiert, teilweise gebaut | `DEFINITION.md` Teil 6, Arten-Editor in `td-ui` |
| Module | Antons sieben stehen | eigene fehlen |
| Vorlagen | Fragebögen stehen | [fragen/](fragen/) |
| Sprache | **steht** | fünfzehn Skills im Marktplatz für Claude Code |

**Der nächste sinnvolle Schritt** ist nicht, alles zu bauen. Es ist, das Vorhandene an **einen** Ort zu räumen und die drei Zusatzfelder zu ergänzen. Ein Baukasten mit acht halben Schichten an vier Orten hilft niemandem.
