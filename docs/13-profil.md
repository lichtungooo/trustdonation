# Das Profil

**Status:** Normativer Entwurf · Überarbeitet am 20.09.2026 (zweite Fassung)

Timo am 18.09.2026: *"Ich will so eine Karte haben, wo alles draufsteht, was eine Stiftung macht. Wo ein Projekt sich komplett vorstellen kann."*

Und am 20.09.2026, nach der ersten Fassung: *"Das ist ja jetzt wirklich dumm Design. Es geht darum, professionelle Profile zu bauen, die diese Fragen, die zu beantworten sind, füllen. Also mit sauberen Reitern, nicht da die Fragen reinzustellen. Schau dir mal modernes Profildesign an."*

---

## Die Fragen sind das Raster, nicht die Oberfläche

Die erste Fassung stellte sechs Abschnitte untereinander, jeder mit seiner Frage als Untertitel: *"Wer ist das · Mit wem habe ich es zu tun?"*. Das ist ein Fragebogen mit Farbe darauf.

**Die Fragen gehören hierher, in die Definition.** Sie sagen, welche Felder ein Profil braucht und in welcher Rangfolge. Auf dem Bildschirm steht die **Antwort**, in der Stimme der Einrichtung.

Das Vorbild steht bei der Software AG-Stiftung selbst. Sie gliedert ihre Seite in fünf Reiter: *Wer wir sind · Warum wir fördern · Wie wir fördern · Was wir fördern · Anträge*. Keine Frage steht auf ihrer Seite; jede ist beantwortet.

---

## Die Anatomie

Vier Teile in dieser Reihenfolge. Sie folgt dem, was ein Mensch in den ersten zehn Sekunden sucht.

```
+----------------------------------------------+
| ######## Farbband in der Hausfarbe ######### |
|  +----+                                      |
|  | SA |   Software AG-Stiftung               |  1. Kopf
|  +----+   Stiftung · fördernd · Darmstadt    |
|           [ Website ]  [ Schreiben ]         |
+----------------------------------------------+
|  FÖRDERUNG        IM JAHR       REICHWEITE   |  2. Kennzahlen
|  20.000-500.000   1,3 Mrd EUR   national     |
+----------------------------------------------+
|  Überblick | Antrag | Geben                  |  3. Reiter
+----------------------------------------------+
|  "Wir suchen und finden Menschen, die        |  4. Inhalt
|   gemeinnützige Ziele verfolgen."            |
|                                              |
|  | Woran Sie erkennen, dass Sie passen       |
|  | Ihr Vorhaben bewegt sich jenseits des     |
|  | Mainstreams ...                           |
|                                              |
|  Förderbereiche                              |
|  (Bildung) (Kinder und Jugend) ...           |
+----------------------------------------------+
```

### 1. Der Kopf

Wer das ist, in einem Blick. Ein Farbband in der Hausfarbe, das Logo darüber, der Name groß, und **eine einzige Meta-Zeile** mit Punkten getrennt: Art · fördernd oder operativ · Sitz.

Daneben die Aktionen: Website, Schreiben. Was ein Mensch als Nächstes tut, steht dort, wo er hinsieht.

**Diese vier Felder erscheinen nirgends sonst**: `foerdererart`, `art`, `sitz`, `website`.

### 2. Die Kennzahlen

Höchstens drei Zahlen, groß gesetzt, nebeneinander. Sie beantworten die Frage, die ein Projekt zuerst hat: *Lohnt sich das Weiterlesen?*

| Bei einem Förderer | Bei einem Projekt |
|---|---|
| Förderung (`summeVon` bis `summeBis`) | Bedarf (`bedarfGesamt`) |
| Im Jahr (`volumenJahr`) | Noch offen (`luecke`) |
| Reichweite (`reichweite`) | Zeitraum (`zeitraum`) |

Eine Kennzahl ohne Angabe fehlt. Wer keine einzige trägt, bekommt keine Leiste.

### 3. Die Reiter

Drei, höchstens vier. Ein Reiter ohne gefüllte Felder erscheint nicht, und wer nur einen Reiter füllt, bekommt gar keine Reiterleiste: Eine Leiste mit einem Reiter ist Zierrat.

| Bei einem Förderer | Was darin steht |
|---|---|
| **Überblick** | `zweck`, `hinweis`, `foerderbereiche`, `zielgruppen`, `bisherGefoerdert` |
| **Antrag** | `antragstellung`, `antragsweg`, `fristen`, `unterlagen`, `antragsportal`, `eigenmittel`, `ansprache`, `mail` |
| **Geben** | `zustiftung`, `spende`, `treuhand` |

| Bei einem Projekt | Was darin steht |
|---|---|
| **Überblick** | `beduerfnis`, `kurz`, `themen`, `zielgruppen`, `wirkung` |
| **Vorhaben** | `bedarfe`, `eigenmittel`, `vorhandenes`, `schritte`, `termine` |
| **Beteiligte** | `anstifter`, `gruppe`, `foerderer`, `zustifter` |

### 4. Der Inhalt

**Der Zweck steht als Aussage**, groß und ohne Beschriftung. Er ist die Stimme der Einrichtung, kein Formularfeld.

**Der Hinweis bekommt seinen eigenen Block**, abgesetzt mit einem farbigen Balken links und der Überschrift *"Woran Sie erkennen, dass Sie passen"*. Er ist das wertvollste Feld der ganzen Karte: Er steht nirgends sonst, und er beantwortet die Frage, die jedes Projekt wirklich hat.

Beim Projekt trägt `beduerfnis` diese Rolle: *"Vierzig Bäche bleiben unbetreut"* zieht, *"wir sind ein Verein für Umweltbildung"* nicht.

**Alles Übrige steht als Definitionsliste**, dicht gesetzt: Beschriftung klein und leise, Wert daneben. Listen erscheinen als Chips.

**Die Quelle steht leise am Fuß**, solange niemand den Eintrag übernommen hat.

---

## Wo ein Profil erscheint

| Was | Wo es steht |
|---|---|
| Profil eines Menschen | Panel rechts, über das Nutzermenü (Antons Spec 12) |
| Profil eines Space | Panel rechts, über die Taste in der Kopfzeile (`?profil={spaceId}`) |
| Profil eines recherchierten Eintrags | in seinem Item-Detail, an der Stelle der Meta-Box |

**Ein Panel, zwei Arten von Profilen.** Wer es öffnet, sieht den, den er gemeint hat: einen Menschen oder eine Einrichtung.

---

## Wer ein Profil trägt

**Wer keinen Bauplan hat, hat kein Profil.** Die Regel steht in `bauplanFuer` und `traegtProfil` (`packages/td-core/src/profil.ts`).

| Wer | Woran erkannt | Bauplan |
|---|---|---|
| Ein Space mit Art | `kind: "stiftung"` oder `"projekt"` | Förderer, Projekt |
| Ein recherchierter Eintrag | `foerdererart` trägt eine Angabe | Förderer |
| Ein Vorhaben | `beduerfnis` trägt eine Angabe | Projekt |
| **Ein Netzwerk** | nichts davon | **keiner** |

Erkannt wird über Feld-Präsenz, nicht über den Typ (Antons Muster 4).

**Zwei Bedingungen für die Taste.** Ein Bauplan greift, und mindestens ein Feld trägt eine Angabe. Eine Taste, die auf eine leere Fläche führt, ist ein gebrochenes Versprechen.

---

## Eine Komponente, kein Modul

| | Modul | Komponente |
|---|---|---|
| **Was** | eine Arbeitsfläche | ein Stück, das woanders erscheint |
| **Wo** | als Reiter in der Kopfzeile | im Panel, im Dialog, auf der Karte, in einer Liste |
| **Wer wählt es** | ein Space, über `Group.data.modules` | niemand: Es erscheint, wo es gebraucht wird |

Die Reiter **im** Profil sind etwas anderes als die Reiter der App. Sie gliedern eine Fläche, sie wechseln keinen Arbeitsort.

**`ProfilFlaeche` ist eine Komponente.** Sie erscheint an vier Orten und liest überall dieselben Felder:

1. **Im Panel rechts**, wenn jemand das Profil eines Space öffnet
2. **Im Item-Detail**, beim Klick auf eine Nadel auf der Karte
3. **Als eigene Seite**, die Landingpage einer Stiftung
4. **In einer Liste**, als Zeile mit den drei Angaben, die zählen

**Ohne Namen kein Kopf.** Im Item-Detail trägt die Ansicht den Titel schon.

**Die Felder messen ihren Kasten.** Container-Anfragen statt Fensterbreite: Eng steht die Beschriftung über dem Wert, breit daneben. Dieselbe Fläche passt damit in ein Panel von 480 Pixeln und auf eine Seite von 768.

---

## Die Regeln

1. **Ein leeres Feld erscheint nicht.** Feld-Präsenz statt Typ-Verzweigung (Antons Muster 4). Eine Karte mit zwanzig Strichen wirkt leerer als eine mit sechs Angaben.
2. **Ein leerer Reiter erscheint nicht.** Dieselbe Regel eine Ebene höher.
3. **Ein einzelner Reiter bekommt keine Leiste.** Eine Reiterleiste mit einem Reiter ist Zierrat.
4. **Ein Nein ist eine Antwort.** „Treuhandstiftung: nein" gehört auf die Karte, denn es erspart jemandem eine Anfrage.
5. **Ein Gedankenstrich ist keine Antwort.** Ein leeres Feld erscheint gar nicht, ein Strich erscheint und sagt nichts.
6. **Keine Frage steht auf dem Bildschirm.** Die Fragen stehen in dieser Datei und im Bauplan. Wer sie anzeigt, macht aus einem Profil einen Fragebogen.
7. **Was andere über die Einrichtung sagen, steht daneben, nie darin.** Bestätigungen und Relationen sind eine eigene Ebene.
8. **Ein recherchierter Eintrag trägt seine Quelle.**
9. **Kein Feld wird erfunden, um die Karte zu füllen.** Was fehlt, fehlt sichtbar.

---

## Verwandt

- `docs/03-datenmodell.md` — die Felder im Einzelnen
- Skill `/td-profil` — der Weg von der Frage zum Feld
- `memory/feedback_design_doktrin.md` — Farbflächen statt Rahmen, seit 12.05.2026
- `DEFINITION.md` Teil 9 im Stack-Repo — warum ein Space das Profil ist
