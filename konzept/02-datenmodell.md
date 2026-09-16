# Datenmodell und rechtliche Leitplanken

*Stand 16.09.2026 · Grundlage: Timos Strategie-Runde vom 16.09.*

> **Hinweis:** Dieses Papier fasst die Leitplanken zusammen, nach denen wir bauen. Es ersetzt keine Rechtsberatung. Bevor die Karte über den Pilot hinaus wächst, lassen wir das Datenmodell einmal anwaltlich prüfen.

## Die Grundregel

Wir dürfen Informationen über Stiftungen sammeln und nutzbar machen. Wir dürfen keine fremden Inhalte, Datenbanken oder persönlichen Kontaktdaten beliebig kopieren.

Die Linie verläuft hier:

> **Fakten extrahieren → selbst strukturieren → Quelle angeben → auf das Original verlinken.**
>
> Nicht: eine Website spiegeln.

Wenn eine Stiftung schreibt „Wir fördern Bildung, Jugend und Naturschutz“, dürfen wir diese Tatsache in unserer eigenen Struktur wiedergeben. So arbeiten bestehende Verzeichnisse auch, etwa die Stiftungssuche des Bundesverbands Deutscher Stiftungen mit Themen, Fördertätigkeit, Antragsmöglichkeit und Deutschlandkarte. Wir bauen darüber eine bessere Interaktionsschicht.

## Vier Dinge, die wir sauber auseinanderhalten

| | Umgang |
|---|---|
| **Fakten** | Frei strukturierbar. Zweck, Region, Summen, Fristen, Antragsweg. |
| **Fremde Texte** | Nicht übernehmen. Kein Fließtext von der Website, keine kompletten Förderbedingungen, keine Fotos, keine Logos ohne Erlaubnis. Datenbanken genießen eigenen Schutz. |
| **Personenbezogene Daten** | Nur mit Rechtsgrundlage. Siehe unten. |
| **Bewertungen** | Gar nicht. Keine Sterne, keine Ampeln. |

## Kontaktdaten: der wichtigste Unterschied

`info@stiftung-xyz.de` ist etwas anderes als `max.mustermann@stiftung-xyz.de`.

Eine persönliche Adresse ist ein personenbezogenes Datum. Für die Verarbeitung brauchen wir eine Rechtsgrundlage nach Art. 6 DSGVO. Selbst der Bundesverband veröffentlicht Ansprechpartner mit persönlichen Kontaktdaten nur mit ausdrücklicher Genehmigung.

**Unser Standard:**

1. Allgemeine Kontaktadresse der Stiftung
2. Offizielle Website
3. Offizielles Antragsportal

Eine namentliche Ansprache steht nur dort, wo die Stiftung sie selbst öffentlich als Ansprechpartner ausweist, oder wo sie ihr Profil selbst übernommen hat.

## Werbung per Mail ist ein eigenes Thema

Eine öffentlich angegebene Adresse auf der Karte zu zeigen, ist etwas anderes, als sie für eine Kampagne zu nutzen. Für elektronische Werbung gilt § 7 UWG, der Mails ohne vorherige Einwilligung streng behandelt.

Für die Ansprache der ersten Stiftungen heißt das: persönlicher Erstkontakt mit konkretem Anlass, keine Massenaussendung. Details in [03-stiftungen-ansprechen.md](03-stiftungen-ansprechen.md).

## Felder: Stiftung

| Feld | Typ | Bemerkung |
|------|-----|-----------|
| Name | Text | |
| Sitz | Text | Stadt, Bundesland, Land |
| Position | Geo | für die Karte |
| Stiftungszweck | Text, eigene Zusammenfassung | kein Zitat von der Website |
| Förderbereiche | Tags | aus dem gemeinsamen Vokabular |
| Regionale Reichweite | Tags | lokal, regional, national, international |
| Zielgruppen | Tags | |
| Art | Auswahl | fördernd, operativ, beides |
| Fördersummen | Zahl von, Zahl bis | |
| Antragstellung | Auswahl | ja, nein, offen |
| Antragsfristen | Text oder Datum | laufend, Stichtag, Fenster |
| Antragsweg | Auswahl | offen, Wettbewerb, Anfrage, eingeladen, operativ, Kooperation, Träger-Partnerschaft, Boden |
| Benötigte Unterlagen | Liste | |
| Eigenmittel nötig | ja/nein/teilweise | |
| Ansprache | Text | Funktion statt Name, solange kein Profil übernommen ist |
| Website | URL | |
| Antragsportal | URL | |
| Öffentliche Mail | Mail | allgemeine Adresse |
| Zustiftung möglich | ja/nein | |
| Spende möglich | ja/nein | |
| Bisher gefördert | Tags oder Liste | Themen, keine kopierten Projektbeschreibungen |

## Felder: Projekt

| Feld | Typ |
|------|-----|
| Name, Beschreibung | Text |
| Position, Region | Geo, Tags |
| Themen | Tags aus dem Vokabular |
| Wer macht es | Relation auf Menschen |
| Was soll entstehen | Text |
| Bedarf gesamt | Zahl |
| Finanzierungslücke | Zahl |
| Benötigte Sachleistungen | Liste |
| Benötigtes Know-how | Tags |
| Laufzeit | Zeitraum |
| Eigenmittel | Zahl |
| Förderer | Relation auf Stiftungen |
| Zustifter | Relation auf Menschen |
| Fortschritt | Einträge mit Datum |

## Der Herkunftsblock

Jeder Datensatz trägt ihn. Er löst die Frage „stimmt das noch?“, indem er sie offen beantwortet.

| Feld | Beispiel |
|------|----------|
| Quelle | Stiftung XY |
| Original | Link auf die Seite, von der die Fakten stammen |
| Erfasst | 16.09.2026 |
| Zuletzt geprüft | 16.09.2026 |
| Verifiziert durch | Stiftung, Redaktion oder automatisch |
| Status | aktuell, Prüfung nötig |

Die Karte sagt dann ehrlich: „Diese Angabe wurde vor acht Monaten zuletzt geprüft.“ Das ist wertvoller als eine stille Behauptung.

## So sieht ein Eintrag aus

Kein Ranking, sondern eine Tabelle, aus der jeder selbst schließen kann:

| Kriterium | Angabe |
|-----------|--------|
| Thema | Jugend, Bildung |
| Region | Deutschland |
| Förderart | Projektförderung |
| Antrag | möglich |
| Frist | laufend |
| Eigenmittel | erforderlich |
| Zustiftung | möglich |
| Spende | möglich |
| Ansprache | Stiftung |
| Quelle | Stiftung selbst |
| Geprüft | 16.09.2026 |

## Matching mit Begründung

Das Matching sagt nie „diese Stiftung ist die beste“. Es sagt „möglicherweise passend“ und legt offen, warum:

```
Projekt: Jugendwerkstatt Kassel
Bedarf: 35.000 EUR · Eigenmittel: 5.000 EUR
Themen: Jugend, Handwerk, Bildung · Region: Nordhessen · Laufzeit: 2027

Möglicherweise passende Förderer

Stiftung A
  Thema passt          Jugend, Handwerk
  Region passt         Hessen
  Zielgruppe passt     Jugendliche
  Förderart passt      Projektförderung
  Antrag möglich       offen, laufend
  Größenordnung passt  10.000 bis 50.000 EUR
  Frist passt          laufend
  Quelle               Stiftung A, geprüft 16.09.2026
```

Jede einzelne Zeile hat eine Quelle und ein Datum. Das macht die Aussage belastbar und überprüfbar.

## Die Stiftung übernimmt ihr Profil

Der sauberste Weg, und langfristig der wichtigste Baustein.

1. Wir legen den Datensatz aus öffentlichen Fakten an.
2. Der Eintrag zeigt: **„Ist das Ihr Eintrag? Profil übernehmen.“**
3. Nach der Übernahme pflegt die Stiftung selbst: Förderbereiche, Ansprache, Fristen, Projekte, Förderaufrufe, Zustiftungsmöglichkeiten, Korrekturen.

Damit wird aus einer statischen Datenbank ein lebendes Netzwerk, und die Stiftung hat einen direkten Vorteil davon. Rechtlich verschiebt sich der Eintrag von „unsere Recherche“ zu „ihre eigene Angabe“, was die Lage deutlich entspannt.

## Abbildung auf den Real Life Stack

| Konzept | Im Stack |
|---------|----------|
| Stiftung | Item vom Typ `foundation` (neues Vokabular) mit `position`, plus optional ein eigener Space |
| Projekt | Item vom Typ `project` (existiert), plus meist ein eigener Space |
| Mensch | Profil im Web of Trust, Item `person` |
| Herkunftsblock | Felder in `data`: `source`, `sourceUrl`, `collectedAt`, `checkedAt`, `verifiedBy`, `status` |
| Förderung | RelationRecord zwischen Stiftung und Projekt, mit Betrag und Datum |
| Verbindung (Stufe 1) | bestehende WoT-Attestation aus der realen Begegnung |
| Beitrag (Stufe 2) | RelationRecord Mensch → Projekt mit Qualifier, von beiden bestätigt |
| Vertrauen (Stufe 3) | abgeleitet aus dem Graphen, nie als Zahl gespeichert |
| Profil-Übernahme | Wechsel von `verifiedBy: redaktion` auf `verifiedBy: stiftung` plus Space-Mitgliedschaft |

Was im Stack dafür noch fehlt und mit Anton zu klären ist:

- Ein Vokabular `foundation/v1` mit den Feldern oben (Spec 06, Schema-Composition)
- Der Vertrag Item ↔ Space: Wie hängt das Stiftungs-Item an ihrem Space? (steht als offene Entscheidung in Spec 04)
- Betrag und Datum an einem RelationRecord
- Ob der Herkunftsblock ein allgemeines Muster für recherchierte Items wird. Das wäre auch für die Macher-Map nützlich.

## Verwandt

- [01-modell.md](01-modell.md) Rollen, Vertrauensstufen, Kreislauf
- `30-konzepte/foerder-landschaft/` 280 recherchierte Stiftungen, Tag-Vokabular, Antragswege
