# 02 Vertrauen

**Status:** Normativer Entwurf

Dieses Dokument trennt drei Dinge, die oft in einen Topf geworfen werden. Diese Trennung ist der Kern von trustdonation.

## Die drei Stufen

### Stufe 1: Verbindung

> Person A und Projekt B haben sich tatsächlich getroffen.

Der Handshake in der Realität, von beiden Seiten bestätigt.

Eine Verbindung sagt: Diese Begegnung hat stattgefunden. Sie sagt nichts über Qualität, Zuverlässigkeit oder Absicht.

*Im Stack:* eine Attestation im Web of Trust, ausgestellt bei der Begegnung.

### Stufe 2: Beitrag

> Ich habe tatsächlich etwas beigetragen.

Zeit, Arbeit, Wissen, Material, Organisation, Geld. Eine Aufgabe übernommen, eine Aufgabe erfüllt, von Beteiligten bestätigt.

Ein Beitrag setzt eine Verbindung voraus und fügt etwas hinzu: Es ist etwas geschehen.

*Im Stack:* ein RelationRecord zwischen Mensch und Projekt mit Qualifier (Zeit, Wissen, Material, Geld), von beiden Seiten bestätigt.

### Stufe 3: Vertrauen

> Aus mehreren echten Erfahrungen ist Vertrauen gewachsen.

Diese Stufe vergibt kein Algorithmus und keine Redaktion. Sie entsteht im Netz aus vielen Verbindungen und Beiträgen über Zeit, und sie bleibt nachvollziehbar: wer mit wem was gemacht hat, soweit die Beteiligten das freigeben.

*Im Stack:* abgeleitet aus dem Graphen, **nie als Zahl gespeichert**.

## Die Regeln

1. **Ein Handshake ist kein Vertrauen.** Wer beides gleichsetzt, baut genau den Trust-Score, den wir vermeiden.
2. **Jede Stufe setzt die vorige voraus.** Ein Beitrag ohne Begegnung ist eine Behauptung, kein Nachweis.
3. **Vertrauen wird nie als Zahl gespeichert.** Es entsteht beim Ansehen des Graphen, aus Beziehungen und ihrer Geschichte.
4. **Sichtbarkeit entscheiden die Beteiligten.** Eine Verbindung erscheint nur, wenn beide Seiten sie freigeben.
5. **Keine Bewertung von Organisationen.** Stiftungen und Projekte tragen Fakten, nie Noten (siehe [04-recht.md](04-recht.md) und [05-matching.md](05-matching.md)).
6. **Geld erzeugt keine Stufe.** Eine Gabe ist ein Beitrag wie Zeit oder Material, nicht mehr.

## Was eine Stiftung dadurch sieht

Statt einer Bewertung sieht sie die soziale Wirklichkeit eines Projekts:

| Projekt Jugendwerkstatt | |
|---|---|
| Initiator | Max |
| Projektgruppe | 12 Menschen |
| Reale Begegnungen | 31 |
| Aktive Mitmacher | 18 |
| Zustifter | 4 |
| Förderer | 2 |
| Anstifter | 3 |

Das ist eine andere Informationsqualität als eine gut geschriebene Projektbeschreibung. Hier existiert nicht nur ein Text, hier sind Menschen tatsächlich verbunden und aktiv.

## Der Weg eines Menschen

Der Grund, warum Geld am Ende steht und nicht am Anfang:

```text
Projekt entdecken
  → Interesse zeigen
  → Menschen kennenlernen
  → zum Treffen kommen
  → Handshake                     Stufe 1
  → mitmachen                     Stufe 2
  → Vertrauen entwickeln          Stufe 3
  → 100 Euro beitragen
  → weitererzählen
  → selbst Anstifter werden
  → eigenes Projekt starten
```

Eine Spendenplattform beginnt bei Schritt 8. trustdonation beginnt bei Schritt 1.

## Verwandt

- [01-rollen.md](01-rollen.md) wer sich hier begegnet
- [03-datenmodell.md](03-datenmodell.md) wie Verbindung und Beitrag gespeichert werden
- Stack: [Spec 05 Confirmations and trust](https://github.com/real-life-org/real-life-stack/blob/master/docs/spec/05-confirmations-and-trust.md)
