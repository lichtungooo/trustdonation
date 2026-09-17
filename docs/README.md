# trustdonation Konzept

**Status:** Im Aufbau — **Single Source of Truth** dieses Repositories

Diese Dokumente beschreiben, was trustdonation ist und nach welchen Regeln es gebaut wird. Sie sind der normative Bereich des Repos. Landingpage, Daten und Betrieb folgen ihnen.

**Bei Konflikt zwischen Konzept und Umsetzung gewinnt das Konzept.** Entweder die Umsetzung anpassen oder das Konzept ändern, mit einer Notiz im Pull Request. Nichts führt stillschweigend eine neue Regel ein.

## Die vier Grundsätze

1. **Geld kauft keine Vertrauensbewertung.**
2. **Fakten statt Noten.**
3. **Vertrauen entsteht im Netz, nicht bei uns.**
4. **Die Identität bleibt beim Menschen.**

Wenn ein Vorschlag einen davon verletzt, wird der Vorschlag geändert, nicht der Satz.

## Kern

Die Dokumente bauen in dieser Reihenfolge aufeinander auf.

| Dokument | Status | Zweck |
|---|---|---|
| [00-ueberblick.md](00-ueberblick.md) | Normativer Startpunkt | Was trustdonation ist, worauf es steht, Abgrenzung zu RLS, WoT und RLNP |
| [01-rollen.md](01-rollen.md) | Normativer Entwurf | Die vier Rollen, warum Menschen keine eigene ist, wer wem gibt |
| [02-vertrauen.md](02-vertrauen.md) | Normativer Entwurf | Verbindung, Beitrag, Vertrauen und warum sie getrennt bleiben |
| [03-datenmodell.md](03-datenmodell.md) | Normativer Entwurf | Felder für Stiftung und Projekt, Abbildung auf den Stack |
| [04-recht.md](04-recht.md) | Arbeitsstand | Was wir aufnehmen dürfen, Herkunftsblock, Profil-Übernahme |
| [05-matching.md](05-matching.md) | Normativer Entwurf | Vorschläge mit Begründung, Förderkriterien, Antragswege |
| [06-foerderhilfe.md](06-foerderhilfe.md) | Normativer Entwurf | Menschen, die beim Antrag helfen, der Förderstammtisch, die Hilfe-Tags |

## Arbeit am Netzwerk

| Dokument | Zweck |
|---|---|
| [07-ansprache.md](07-ansprache.md) | Drei Türen, Partnerprogramm, 30-Minuten-Termin, erste Mail |
| [08-pilot.md](08-pilot.md) | Der Pilot, vier Wellen, offene Punkte für den Stack |

## Betrieb und Zusammenarbeit

| Dokument | Zweck |
|---|---|
| [09-betrieb.md](09-betrieb.md) | Server, Container, Domains, Sicherung, was im Notfall hilft |
| [10-zusammen-testen.md](10-zusammen-testen.md) | Anmelden, verifizieren, gemeinsam arbeiten. Der Ablauf für ein Treffen |
| [11-zusammen-arbeiten.md](11-zusammen-arbeiten.md) | Zu dritt bauen: wer welches Stück nimmt, wo der Stand steht, wo Entscheidungen fallen |
| [12-baukasten.md](12-baukasten.md) | Woraus wir bauen: acht Schichten von Rohstoffen bis Sprache, für Landingpage, App und Web of Trust |

## Fragebögen

Jede Frage gehört zu genau einem Feld aus [03-datenmodell.md](03-datenmodell.md). Die Bögen dienen dreifach: als Leitfaden am Tisch, als Durchlauf in der App, als Feldliste.

| Bogen | Für |
|---|---|
| [fragen/projekt.md](fragen/projekt.md) | Ein Projekt anlegen: 14 W-Fragen in drei Runden |
| [fragen/stiftung.md](fragen/stiftung.md) | Einen Stiftungseintrag anlegen: 13 W-Fragen, Recherche und Übernahme |
| [fragen/stiftungsgespraech.md](fragen/stiftungsgespraech.md) | Der erste Termin mit einer Stiftung: sieben Fragen und Protokollbogen |
| [fragen/beispiel-projekt.md](fragen/beispiel-projekt.md) | **Gelöst:** trustdonation selbst durch den Projektbogen |
| [fragen/beispiel-stiftung.md](fragen/beispiel-stiftung.md) | **Gelöst:** ein recherchierter Stiftungseintrag, Schritt für Schritt |

## Nachschlagen

- [glossar.md](glossar.md) Begriffe mit Verweis auf die Stelle, an der sie definiert sind

## Was hier nicht steht

- Kryptografie, DIDs, Signaturformate: [Web of Trust][wot]
- Architektur des Baukastens, Connectoren, Module: [Real Life Stack][rls]
- Soziale Semantik von Begegnungen und Quests: RLNP-Konzept im Stack-Repo
- Rechtsform und Satzung des Vereins

[rls]: https://github.com/real-life-org/real-life-stack
[wot]: https://github.com/antontranelis/web-of-trust
