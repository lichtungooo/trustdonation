# Pilot und Umsetzung

*Stand 16.09.2026 · Grundlage: Timos Strategie-Runde vom 16.09.*

## Der Grundgedanke

Wir warten nicht, bis die Software fertig ist. Wir beweisen zuerst eine Kette:

> Projekt A → Stiftung B → Anstifter C → Zustifter D → reale Umsetzung.

Vieles davon darf am Anfang von Hand laufen. Für Stiftungen ist ein funktionierender Fall überzeugender als ein fertiger Tech-Stack.

## Der Pilot

| Größe | Zahl |
|-------|------|
| Stiftungen | 10 |
| Projekte | 20 |
| Community | 100 Menschen |
| Anstifter | 5 |
| Konkrete Förderfälle | 3 bis 5 |

Was der Pilot beweisen soll:

1. Ein Projekt findet über Tags eine Stiftung, die es vorher nicht kannte.
2. Ein Mensch kommt über die Karte zu einem Projekt, trifft die Gruppe und macht mit.
3. Aus dieser Begegnung wird ein Beitrag, und daraus später eine Gabe.
4. Eine Stiftung übernimmt ihr Profil und pflegt es selbst.
5. Ein Anstifter bringt ein Vorhaben von der Idee bis zur Finanzierung.

## Vier Wellen

### Welle 1: Sichtbarkeit (jetzt bis Ende Oktober)

Die Karte trägt Stiftungen und Projekte, mit Herkunftsblock.

- Vokabular `foundation/v1` im Stack (mit Anton)
- 80 Stiftungen mit hoher Passung aus der Förder-Landschaft eintragen, je mit Quelle und Prüfdatum
- Erste 20 Projekte aufnehmen
- Landing: die Karte zeigt echte Pins statt der Illustration
- Profil-Übernahme als Knopf am Eintrag

**Was gebraucht wird:** das Vokabular, ein Import-Weg für die JSON-Daten, eine Redaktions-Rolle.

### Welle 2: Matching mit Begründung (November)

Die Liste „möglicherweise passende Förderer“ mit Zeile für Zeile nachvollziehbarer Begründung.

- Score aus Themen, Region, Zielgruppe, Förderart, Antragsweg, Größenordnung, Frist
- Jede Zeile zeigt Quelle und Prüfdatum
- Umgekehrte Richtung: Stiftung sieht passende Projekte
- Filter auf der Karte: Förderkriterium, Region, Antragsweg

**Was gebraucht wird:** ein Modul oder eine Linse im Stack, die zwei Item-Typen gegeneinander rechnet.

### Welle 2b: Förderhilfe (parallel zu Welle 2)

Läuft ohne neue Technik, mit den Tags aus [06-foerderhilfe.md](06-foerderhilfe.md).

- Fünf Menschen tragen ihr Können ein: `#antragshilfe`, `#finanzierungsplan`, `#projektskizze`
- Drei Pilotprojekte tragen denselben Bedarf
- Ein Förderstammtisch in Nordhessen, mit jemandem aus einer Stiftung der ersten Welle
- Ein Antrag, der dadurch besser wird. Das ist der Beweis fürs nächste Gespräch

### Welle 3: Menschen und Beiträge (Dezember)

Der Teil, der trustdonation von einem Verzeichnis unterscheidet.

- Mensch entdeckt Projekt, zeigt Interesse, kommt zum Treffen
- Handshake bestätigt die Verbindung (existiert im Web of Trust)
- Beitrag als Relation mit Qualifier: Zeit, Wissen, Material, Geld
- Projektseite zeigt reale Begegnungen, aktive Mitmacher, Beiträge
- Direkte Spende an ein Projekt, ähnlich Startnext, aber als Folge einer Beziehung

**Was gebraucht wird:** Betrag und Datum an RelationRecords, eine Zahlungsanbindung, die Anzeige der drei Stufen.

### Welle 4: Der Kreis schließt sich (Q1 2027)

- Anstifter-Weg von der Idee bis zur Gruppe
- Bedarfe eines Projekts: Geld, Sachleistung, Know-how, Raum
- Zustifter sucht nach Thema und Region und sieht die Finanzierungslücke
- Wirkung zurück auf die Karte

## Was Anton entscheiden muss

Aus [03-datenmodell.md](03-datenmodell.md), gesammelt für das nächste Gespräch:

1. **Vokabular `foundation/v1`**: eigener Typ oder `project` mit anderem Schema?
2. **Item ↔ Space**: Wie hängt das Stiftungs-Item an ihrem Space? Steht als offene Entscheidung in Spec 04.
3. **Betrag und Datum am RelationRecord**: für Förderung, Zustiftung, Spende.
4. **Herkunftsblock als allgemeines Muster** für recherchierte Items. Nützt auch der Macher-Map.
5. **Redaktions-Rolle**: Wer darf einen Eintrag anlegen, den die Organisation noch nicht übernommen hat?

## Was sofort geht, ohne Code

- Die 10 Stiftungen der ersten Welle ansprechen ([07-ansprache.md](07-ansprache.md))
- Die sieben Fragen stellen und die Antworten sammeln
- Einen Förderfall von Hand durchspielen und dokumentieren
- Entwürfe der Einträge als PDF oder Link zeigen und übernehmen lassen

Diese Arbeit erzeugt genau das Material, mit dem Welle 1 und 2 richtig gebaut werden.

## Offene Entscheidungen für Timo

1. **Direkte Spende an Projekte:** ab wann, über welchen Zahlungsweg, und wie verhindern wir, dass Geld zum Einstieg wird statt zum Ergebnis?
2. **Anwaltliche Prüfung** des Datenmodells vor dem Start von Welle 1.
3. **Wer pflegt die Redaktion?** Die 80 Einträge brauchen einen Menschen, der Quellen prüft und Prüfdaten setzt.

## Verwandt

- [01-rollen.md](01-rollen.md), [03-datenmodell.md](03-datenmodell.md), [07-ansprache.md](07-ansprache.md)
- Datenbasis: 280 recherchierte Stiftungen im Workspace
- [fragen/beispiel-projekt.md](fragen/beispiel-projekt.md) trustdonation durch den eigenen Bogen
