---
name: td-definieren
description: "Eine neue Sache fuer trustdonation definieren, bevor sie Code wird. Das Raster (welche Frage, welche eine Quelle, welche Schicht, was bei Unbekanntem), Antons sechs Muster als Pruefliste, und der Weg von der Definition ueber den Test zum Bau."
---

# Eine Sache definieren

Erst definieren, dann bauen. Das ist Regel 1 unserer Arbeit, und sie hat einen Grund: Bis hierher haben wir gebaut und danach beschrieben. Das traegt eine Runde weit. Ab der zweiten laufen die Listen auseinander, und niemand weiss mehr, welche Stelle die Wahrheit hat.

Dieser Skill greift, **bevor** eine neue Sache Code wird: ein Feld, ein Typ, ein Modul, ein Bereich, ein Register.

## Das Raster

Jede Definition beantwortet vier Fragen. Sie steht als Abschnitt in `docs/DEFINITION.md`.

### 1. Welche Frage beantwortet das?

Eine Frage, in einem Satz, in der Form *„Was folgt daraus, dass ...?"*

- Was folgt daraus, dass ein Item diesen `type` traegt?
- Was folgt daraus, dass ein Space dieses Modul fuehrt?
- Was folgt daraus, dass ein Space als Stiftung gefuehrt wird?
- Was folgt daraus, dass ein Datensatz dieses Feld traegt?

Laesst sich die Frage nicht in einem Satz sagen, sind es zwei Sachen. Dann werden es zwei Abschnitte.

### 2. Wo ist die eine Quelle?

Genau eine Stelle beantwortet die Frage. Jede Flaeche, die aufzaehlt, anbietet, benennt oder anzeigt, leitet ihre Liste **daraus** ab.

Nenne die Stelle beim Namen: Datei, Funktion, Register. Eine zweite Aufzaehlung derselben Sache ist ein Fehler, kein Kompromiss.

### 3. Welche Schicht haelt was?

Zwei Schichten entlang der Paketgrenze, wie bei Anton:

| Schicht | Paket | haelt | aendert sich wenn |
|---|---|---|---|
| Manifest | `td-core`, ohne UI | Identitaet, Bindung, Kanten | die Bedeutung sich aendert |
| Darstellung | `td-ui` | Name, Icon, Widgets, Slots | das Aussehen sich aendert |

Die Abhaengigkeit zeigt in eine Richtung: `td-ui` kennt `td-core`, nie umgekehrt.

### 4. Was passiert bei Unbekanntem?

Ein unbekannter Eintrag **bleibt erhalten** und **faellt sichtbar zurueck**. Nie stillschweigend entfernen, nie leer, nie kaputt.

Das ist die Regel, die Erweiterbarkeit erst moeglich macht. Wer sie bricht, bestraft jeden, der etwas Eigenes baut.

## Antons sechs Muster als Pruefliste

Gehe sie durch, bevor der Abschnitt steht.

1. **Ein Register je Frage, eine Quelle.** Baue ich ein zweites Register fuer eine Frage, die schon beantwortet ist?
2. **Zwei Schichten entlang der Paketgrenze.** Zieht meine Definition React in ein UI-freies Paket?
3. **Schichten Core, App, Space, additiv.** Wie wird zusammengesetzt? Eine vergebene Id ist ein Konflikt, ein Fragment ergaenzt additiv, ein gesetztes Skalar darf nicht ueberschrieben werden. **Kein Shadowing, weder still noch ausdruecklich.**
4. **Feld-Praesenz statt Typ-Verzweigung.** Verzweigt irgendwo etwas nach `type`? Dann ist die Definition falsch herum: Nicht das Feld sucht die Flaeche, die Flaeche erklaert, was sie darstellen kann.
5. **Unbekanntes bleibt erhalten.** Siehe Frage 4.
6. **Die Spec gewinnt.** Widerspricht meine Definition irgendwo `docs/spec/`? Dann wird meine berichtigt.

## Die drei Regeln, die aus dem Projekt kommen

Zusaetzlich zu Antons Mustern:

1. **Nichts wird hart verdrahtet, was eine Instanz unterscheiden kann.** Namen, Arten, Farben, Domains, Felder kommen aus Daten oder Laufzeit-Konfiguration. Eine Liste im Code, die anderswo anders aussehen muesste, ist ein Fehler.
2. **Keine Bewertungen.** Keine Punkte, keine Sterne, keine Ranglisten, keine Passungszahl. Wo ein Vergleich noetig ist: **Gruende** nennen, der Mensch entscheidet.
3. **Was ein Mensch eingibt, steht in `data`.** Die obersten Felder gehoeren dem Core. Dasselbe fuer `Group.data`.

## Der Abschnitt

So sieht er aus:

```markdown
## Teil <n>: <Name>

**Frage, die dieser Abschnitt beantwortet:** Was folgt daraus, dass ...?

<Ein Absatz: was heute daraus folgt, was kuenftig daraus folgen soll,
und warum die Loesung so aussieht.>

### Eintrag

| Feld | Schicht | Zweck |
|---|---|---|
| ... | ... | ... |

### Regeln

1. <Die eine Quelle.>
2. <Was die Schichten halten.>
3. <Was bei Unbekanntem passiert.>
4. <Was die Sache ausdruecklich NICHT traegt.>
...
```

Der letzte Punkt ist wichtig und wird gern vergessen: **Was traegt die Sache nicht?** Ein Register, das Rechte traegt, ist kaputt. Eines, das Aktivierung traegt, auch. Schreib es hin.

## Dann erst der Bau

1. Abschnitt in `docs/DEFINITION.md`.
2. **Ein Test fuer jede Regel, die eine Liste betrifft.** Genau dort laufen Dinge auseinander. Nicht fuer alles einen Test, aber fuer die Listen.
3. Bau, nach `docs/ARCHITEKTUR.md` Teil 3 (was gehoert in welches Paket).
4. Aendert der Bau Antons Code: Skill `td-naht`.
5. Eintrag in `memory/stand_trustdonation.md`, mit dem, was schiefging.

## Wenn eine Definition sich als falsch erweist

Berichtigen, nicht danebenlegen. Eine zweite Definition derselben Sache ist genau der Fehler, gegen den das ganze Verfahren gebaut ist. Der alte Abschnitt wird ueberschrieben, und ein Satz haelt fest, was sich geaendert hat und warum.

## Verwandt

- `docs/DEFINITION.md` Teil 2 (die sechs Muster) und Teil 3 (unsere Regeln)
- `docs/ARCHITEKTUR.md` Teil 3 (Paketschnitt)
- Skill `td-naht`, Skill `klare-sprache` fuer die Sprache der Dokumente
