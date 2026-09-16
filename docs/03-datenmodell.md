# 03 Datenmodell

**Status:** Normativer Entwurf

Die Felder für Stiftung und Projekt und ihre Abbildung auf den Real Life Stack. Die rechtlichen Grenzen stehen in [04-recht.md](04-recht.md).

## Stiftung

| Feld | Typ | Bemerkung |
|---|---|---|
| `name` | Text | |
| `sitz` | Text | Stadt, Bundesland, Land |
| `position` | GeoJSON Point | für die Karte |
| `zweck` | Text | eigene Zusammenfassung, kein Zitat |
| `foerderbereiche` | Tags | aus dem gemeinsamen Vokabular |
| `reichweite` | Tags | lokal, regional, national, international |
| `zielgruppen` | Tags | |
| `art` | Auswahl | fördernd, operativ, beides |
| `summeVon`, `summeBis` | Zahl | |
| `volumenJahr` | Zahl | wenn öffentlich bekannt |
| `antragstellung` | Auswahl | ja, nein, offen |
| `fristen` | Text oder Datum | laufend, Stichtag, Fenster |
| `antragsweg` | Auswahl | offen, Wettbewerb, Anfrage, eingeladen, operativ, Kooperation, Träger-Partnerschaft, Boden |
| `unterlagen` | Liste | |
| `eigenmittel` | ja, nein, teilweise | |
| `ansprache` | Text | Funktion statt Name, solange kein Profil übernommen ist |
| `website`, `antragsportal` | URL | |
| `mail` | Mail | allgemeine Adresse |
| `zustiftung`, `spende`, `treuhand` | ja, nein | |
| `bisherGefoerdert` | Tags oder Liste | Themen, keine kopierten Projektbeschreibungen |
| `hinweis` | Text | „Woran erkennt ein Projekt, dass es zu uns passt“, in ihren Worten |

Dazu der Herkunftsblock aus [04-recht.md](04-recht.md).

## Projekt

| Feld | Typ |
|---|---|
| `name`, `kurz` | Text |
| `beduerfnis` | Text: was fehlt hier ohne dieses Projekt |
| `position`, `region` | GeoJSON Point, Tags |
| `themen` | Tags, drei bis sechs |
| `zielgruppen` | Tags |
| `anstifter`, `gruppe` | Relationen auf Menschen |
| `bedarfe` | Liste, je Eintrag mit Art: Hände, Wissen, Sachen, Raum |
| `bedarfGesamt`, `eigenmittel`, `luecke` | Zahl |
| `zeitraum`, `termine` | Zeitraum, Daten |
| `schritte` | Liste |
| `vorhandenes` | Liste: Zusagen, Genehmigungen, Material, Räume |
| `wirkung` | Liste: zwei bis drei nachprüfbare Dinge |
| `foerderer`, `zustifter` | Relationen |
| `fortschritt` | Einträge mit Datum |

## Abbildung auf den Real Life Stack

| Konzept | Im Stack |
|---|---|
| Stiftung | Item vom Typ `foundation` (neues Vokabular) mit `position`, optional ein eigener Space |
| Projekt | Item vom Typ `project` (existiert), meist plus eigener Space |
| Mensch | Profil im Web of Trust, Item `person` |
| Herkunftsblock | Felder in `data`: `source`, `sourceUrl`, `collectedAt`, `checkedAt`, `verifiedBy`, `status` |
| Förderung | RelationRecord Stiftung → Projekt, mit Betrag und Datum |
| Verbindung (Stufe 1) | WoT-Attestation aus der realen Begegnung |
| Beitrag (Stufe 2) | RelationRecord Mensch → Projekt mit Qualifier, beidseitig bestätigt |
| Vertrauen (Stufe 3) | abgeleitet aus dem Graphen, nie gespeichert |
| Profil-Übernahme | `verifiedBy` wechselt von `redaktion` auf `stiftung`, plus Space-Mitgliedschaft |

## Offene Punkte für den Stack

Diese fünf gehören ins nächste Gespräch mit Anton. Keiner davon ist trustdonation-spezifisch; alle nützen auch anderen Instanzen.

1. **Vokabular `foundation/v1`** mit den Feldern oben. Eigener Typ oder `project` mit anderem Schema? Siehe [Spec 06 Schema-Composition][s06].
2. **Vertrag Item ↔ Space.** Wie hängt das Stiftungs-Item an ihrem Space? Steht als offene Entscheidung in [Spec 04][s04].
3. **Betrag und Datum am RelationRecord**, für Förderung, Zustiftung und Spende. Siehe [Spec 08][s08].
4. **Herkunftsblock als allgemeines Muster** für recherchierte Items. Nützt auch der Macher-Map.
5. **Redaktions-Rolle.** Wer darf einen Eintrag anlegen, den die Organisation noch nicht übernommen hat?

[s04]: https://github.com/real-life-org/real-life-stack/blob/master/docs/spec/04-items-relations-groups-spaces.md
[s06]: https://github.com/real-life-org/real-life-stack/blob/master/docs/spec/06-schema-composition.md
[s08]: https://github.com/real-life-org/real-life-stack/blob/master/docs/spec/08-relation-records.md

## Verwandt

- [04-recht.md](04-recht.md) was wir aufnehmen dürfen und was nicht
- [fragen/projekt.md](fragen/projekt.md), [fragen/stiftung.md](fragen/stiftung.md) je Frage ein Feld
- Datenbasis: 280 recherchierte Stiftungen, Tag-Vokabular, acht Antragswege (Workspace `30-konzepte/foerder-landschaft/`)
