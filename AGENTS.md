# AGENTS.md

Dieses Repository ist agentenlesbar. Es setzt keine bestimmte Agenten-Laufzeit voraus.

Lies zuerst diese Datei, dann den Konzept-Index in [docs/README.md](./docs/README.md).

## Zweck des Repositories

trustdonation ist eine **Instanz** des [Real Life Stack][rls]: eine Karte, auf der Stiftungen, Projekte und Menschen einander finden, mit einem Matching, das jeden Vorschlag begründet.

```text
trustdonation (Landing, Konzept, Daten)
  → Real Life Stack (rls-app Image)
    → Web of Trust (Identität, Begegnung, Sync)
```

**Hier liegt kein Stack-Code.** Die App kommt als fertiges Image aus `ghcr.io/real-life-org/rls-app`. Wer eine Änderung am Baukasten braucht, öffnet einen Pull Request im [Stack-Repo][rls] und verweist von hier darauf.

## Quelle der Wahrheit

- Konzept-Index: [docs/README.md](./docs/README.md)
- Überblick und Abgrenzung: [docs/00-ueberblick.md](./docs/00-ueberblick.md)
- Rollen: [docs/01-rollen.md](./docs/01-rollen.md)
- Vertrauen: [docs/02-vertrauen.md](./docs/02-vertrauen.md)
- Datenmodell: [docs/03-datenmodell.md](./docs/03-datenmodell.md)
- Recht: [docs/04-recht.md](./docs/04-recht.md)
- Matching: [docs/05-matching.md](./docs/05-matching.md)
- Begriffe: [docs/glossar.md](./docs/glossar.md)

Bei Konflikt zwischen Konzept und Umsetzung gewinnt das Konzept. Keine stillschweigend neue Regel: lieber eine kleine Korrektur, eine klare PR-Notiz oder ein Issue.

## Die vier Grundsätze

Sie sind normativ. Ein Vorschlag, der einen davon verletzt, wird geändert.

1. **Geld kauft keine Vertrauensbewertung.** Kein Partner bekommt eine bessere Platzierung im Matching.
2. **Fakten statt Noten.** Keine Sterne, keine Ampeln, keine gespeicherte Bewertung an einer Organisation.
3. **Vertrauen entsteht im Netz, nicht bei uns.** Vertrauen wird nie als Zahl gespeichert.
4. **Die Identität bleibt beim Menschen.** Schlüssel auf dem Gerät, Profil wandert mit.

## Regeln für Daten

Vor der Veröffentlichung eines recherchierten Eintrags gilt die Checkliste in [docs/04-recht.md](./docs/04-recht.md):

- Eigene Zusammenfassung statt Zitat, kein Logo, kein fremdes Foto
- Allgemeine Kontaktadresse statt persönlicher
- Herkunftsblock vollständig, `checkedAt` gesetzt
- Keine Bewertung im Eintrag
- Link auf das Original sichtbar

Ein Eintrag über eine reale Organisation geht erst online, nachdem sie ihn gesehen hat. Beispiele in der Dokumentation nutzen erfundene Organisationen.

## Sprache

- Deutsch, echte Umlaute (ä, ö, ü, ß). Bezeichner, Pfade und Dateinamen bleiben ASCII.
- Keine Gedankenstriche, weder – noch —. Stattdessen Punkt, Doppelpunkt, Komma, Klammer.
- Kein Gendern mit Sonderzeichen; wo ein Text alle ansprechen soll, wird neutral formuliert.
- Ton: modern, professionell, zugänglich. Kurze Sätze, konkrete Wörter, Zahlen und Namen statt Abstraktion.

## Landingpage

Freies HTML unter `landing/`, kein Build-Schritt.

- Jeder sichtbare Text trägt `data-t="schluessel"`, das Wörterbuch steht in `landing/site.js` (`var T`).
- Drei Sprachen: `de`, `en`, `es`. Alle drei tragen dieselben Schlüssel.
- Neun Sprachstile unter `landing/stile/<stil>.json`, je eine Datei, dieselben Schlüssel wie `de`. Fehlende Schlüssel fallen auf `de` zurück.
- Vor jedem Commit: `node --check landing/site.js`.

## Betrieb

```bash
docker compose up -d      # liest .env, zieht das gepinnte Image
```

Deploy auf dem Server: `git pull`. Kein Build, kein scp.

Drei Update-Kanäle, siehe [README.md](./README.md):

| Was | Wie |
|---|---|
| App | `RLS_IMAGE_TAG` in der `.env` hochziehen |
| Instanz-Vorlage | `git fetch upstream && git merge upstream/main` |
| Diese Seite | `git pull` |

## Offene Punkte für den Stack

Fünf Punkte warten auf eine Entscheidung im Stack-Repo, alle in [docs/03-datenmodell.md](./docs/03-datenmodell.md) beschrieben: Vokabular `foundation/v1`, Vertrag Item ↔ Space, Betrag und Datum am RelationRecord, Herkunftsblock als allgemeines Muster, Redaktions-Rolle.

[rls]: https://github.com/real-life-org/real-life-stack
