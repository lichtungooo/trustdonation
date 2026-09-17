---
name: sprach-stile
description: "Eine Stimme wählen und einen Text darin schreiben oder umschreiben: klar, klartext, kraftvoll, herzens-sprache, kindgerecht, tiefstapelei, groessenwahn, schamanisch, soziologen-sprech, marktschreier. Greift bei /sprach-stile <stil>, bei der Frage nach den Stilrichtungen, und wenn ein Text in einer bestimmten Stimme klingen soll."
---

# Sprach-Stile

Ein Inhalt, viele Stimmen. Dieser Skill sammelt die Sprachformen des Real Life Network an einem Ort. Jede Stimme hat eine eigene Referenz mit Haltung, Regeln, Wortschatz und Beispielen. Der Skill wählt die Stimme, die Referenz führt die Hand.

## Aufruf

- `/sprach-stile` ohne Angabe: die Tabelle unten zeigen und fragen, welche Stimme es sein soll.
- `/sprach-stile <stil>` und danach der Text oder der Pfad: den Text in dieser Stimme schreiben oder umschreiben.
- `/sprach-stile <stil> vergleichen`: denselben Absatz in der gewählten und in der klaren Stimme nebeneinander stellen.
- Die Frage "welche Stilrichtungen gibt es?" beantwortet die Tabelle.

## Die Stimmen

| Stil-Id | Name | Klang | Vorbilder | Wann |
|---------|------|-------|-----------|------|
| `klar` | Klar | alltagstauglich, warm, leicht | Kant, Goethe, Schiller im Kern, Arne im Ton | Standard für alles, was aus dem Real Life Network in die Welt geht |
| `klartext` | Klartext | modern, professionell, zugänglich | Wolf Schneider, Barbara Minto, gute Produkttexte | Erklärungen, Landingpages, Produkttexte, Anleitungen, FAQ, Mails: alles, was jemand liest, um etwas zu verstehen oder zu tun |
| `kraftvolle-sprache` | Kraftvolle Sprache | klar, pathosfähig, imperativisch, tragend | Schiller, Goethe, Kant, Schweitzer | Manifest-Stücke, Grundsatz-Passagen, Titel mit Gewicht |
| `herzens-sprache` | Herzens-Sprache | weich, atmend, einladend | Eckhart, Hildegard, Rumi, Rilke | Friedenstexte, Meditation, Willkommen, Einladung |
| `kindgerecht` | Kindgerecht | warm, staunend, einfach | Sendung mit der Maus, logo!, Löwenzahn | Erklärungen für Kinder, einfache Sprache, Onboarding |
| `tiefstapelei` | Tiefstapelei | zweifelnd, kleinlaut, entschuldigend, liebenswert | Charlie Brown, Marvin, I-Aah, Loriot | Zerrspiegel, Comedy, Gegenmittel zum Größenwahn |
| `groessenwahn` | Größenwahn | welterobernd, pathetisch, mit Augenzwinkern | Musk, Jobs, Napoleon, Marvel | Vision groß denken, Pitch, Launch |
| `schamanisch` | Schamanisch | zeremoniell, zyklisch, animistisch | Lakota, Hopi, Black Elk, Häuptling Seattle | Zeremonie, Ritual, Texte am Feuer |
| `soziologen-sprech` | Soziologen-Sprech | theoriegesättigt, hypotaktisch, augenzwinkernd ernst | Habermas, Luhmann, Bourdieu | akademische Analyse, Zerrspiegel für Förderanträge |
| `marktschreier` | Marktschreier | laut, theatralisch, direkt, herzlich | Hamburger Fischmarkt, Aale-Dieter | Werbetext, Aufmerksamkeit, Jahrmarkt |

Zu `klartext` gehört eine zweite Ebene: [reference/klartext-werkstatt.md](reference/klartext-werkstatt.md) mit den Lehrern, dem Prüfraster nach dem Hamburger Verständlichkeitsmodell, den Tiefen-Regeln, Leserprofilen und Textsorten. Sie wird gelesen, wenn ein Text länger als eine Seite ist oder nicht sitzt.

**Im Zweifel zwischen `klar` und `klartext`:** Geht es um das **Warum** (Haltung, Manifest, Einladung), nimm `klar`. Geht es um **Was und Wie** (Erklärung, Produkt, Anleitung), nimm `klartext`.

Jede Stimme liegt unter `reference/<stil-id>.md`. **Vor dem Schreiben die Referenz der gewählten Stimme lesen**, danach schreiben, dann die Selbst-Prüfung am Ende der Referenz durchgehen.

## Was in jeder Stimme gilt

1. **Echte Umlaute** im Text: ä, ö, ü, ß. Identifier, Pfade und Dateinamen bleiben ASCII.
2. **Keine Gedankenstriche**, weder – noch —. Stattdessen Punkt, Doppelpunkt, Komma, Klammer.
3. **Fakten bleiben wahr.** Zahlen, Namen, Beträge, Fristen und Produktnamen (trustdonation, Real Life Network e.V., Web of Trust) ändern sich in keiner Stimme. Größenwahn übertreibt im Ton, nie bei Zahlen.
4. **Rollen bleiben erkennbar.** Wer im Original Projekt, Stiftung, Stifter, Zustifter oder Mensch ist, bleibt es auch in der Stimme, egal wie sie ihn nennt.
5. **Kein Gendern, keine Emoji, kein KI-Pathos** (keine Triplets, keine "Aus X wird Y"-Wendungen, keine Pathos-Closer).
6. **Form bleibt Form.** HTML-Tags, Markdown-Struktur, Platzhalter, Pfeile "→" und Zeilenumbrüche stehen nach dem Umschreiben an derselben Stelle.
7. **Länge in der Nähe des Originals.** Höchstens 40 Prozent länger; Schaltflächen und Menüpunkte höchstens vier Wörter; Untertitel eine Zeile.

## Arbeitsweise

1. Stimme klären. Fehlt sie, fragen oder aus dem Auftrag ableiten ("für Kinder" ist kindgerecht, "am Feuer" ist schamanisch, "für den Förderantrag" ist klar oder soziologen-sprech).
2. `reference/<stil-id>.md` lesen.
3. Den Originaltext ganz lesen, Fakten und Rollen markieren.
4. Schreiben. Absatz für Absatz, in der Stimme, mit ihrem Wortschatz-Anker.
5. Selbst-Prüfung der Referenz durchgehen, dann die sieben Regeln oben.
6. Bei Wörterbüchern (JSON mit Schlüsseln, wie `stile/<stil>.json` der trustdonation-Landing): exakt dieselben Schlüssel, gültiges JSON, dann mit einem Skript prüfen (Schlüsselmengen gleich, keine Striche, Tags gezählt).

## Alle ansprechen

Soll ein Text alle ansprechen, ohne jemanden vor den Kopf zu stoßen, greift zusätzlich der Skill `/gendern`. Er legt sich über jede Stimme und ersetzt sie nicht.

## Herkunft

Die Stimmen sind aus `rln-alle-sprachformen.md` gewachsen: zwölf Fassungen des Real-Life-Network-Textes, geschrieben von Timo und Anton als Sprachexperiment. Drei Fassungen daraus (Walla-Digger, Russen-Sprech, Sprach-Matsch) sind bewusst noch keine Stimmen dieses Skills; sie kommen dazu, sobald jemand sie braucht.

Erste Anwendung: die Landingpage `wir.ooo` (trustdonation), auf der die Leser Sprache und Sprachstil selbst wählen. Die deutschen Fassungen liegen dort als `stile/<stil-id>.json`, eine Datei je Stimme.
