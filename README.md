# trustdonation

**Infrastruktur für vertrauensbasierte Förderung.** Stiftungen, Projekte, Anstifter, Zustifter und Menschen finden auf einer Karte zueinander.

Getragen vom [Real Life Network e.V.](https://reallife.network) · gebaut auf dem [Real Life Stack](https://github.com/real-life-org/real-life-stack) · Vertrauensschicht ist das Real Life Trust Protokoll.

| | |
|---|---|
| Domain | trustdonation.org *(DNS in Arbeit)* |
| Baustelle | <https://wir.ooo> |
| Konzept | [konzept/INDEX.md](konzept/INDEX.md) |

## Der Satz

> trustdonation baut eine Infrastruktur, mit der Stiftungen ihre Förderwirkung erhöhen, weil passende Projekte, Menschen, Anstifter und Zustifter leichter zusammenfinden.

Keine Spendenplattform. Eine Verbindungsschicht zwischen Kapital, Menschen, Organisationen und realen Vorhaben. Geld ist nicht der Einstieg, sondern ein Ergebnis einer Beziehung.

## Die vier Grundsätze

1. **Geld kauft keine Vertrauensbewertung.** Partner bekommen Status und Mitsprache, keine bessere Platzierung im Matching.
2. **Fakten statt Noten.** Kriterien, Quelle, Prüfdatum. Keine Sterne, keine Ampeln, keine Bewertung von Organisationen.
3. **Vertrauen entsteht im Netz, nicht bei uns.** Wir stellen kein Zertifikat aus, wir machen nachvollziehbar, was passiert ist.
4. **Die Identität bleibt beim Menschen.** Schlüssel auf dem Gerät, Profil wandert mit.

## Was hier liegt

```
landing/      die Landingpage, wird auf / ausgeliefert
  stile/      neun Sprachstile als Wörterbuch, je eine JSON-Datei
  logo/       Wortmarke und Signet
  fonts/      selbst gehostet, keine Anfrage an Dritte
konzept/      Modell, Datenmodell, Ansprache, Pilot, Fragebögen
branding/     theme.json (Farbtokens) und favicon.svg für die App
docker-compose.yml
.env.example  Vorlage; die echte .env steht auf dem Server
```

**Kein Stack-Code.** Die App kommt als fertiges Image aus `ghcr.io/real-life-org/rls-app`. Alles hier ist Konfiguration und Inhalt (siehe [Spec 11][spec]).

[spec]: https://github.com/real-life-org/real-life-stack/blob/master/docs/spec/11-runtime-config-und-branding.md

## Drei Arten von Updates

| Was | Woher | Wie |
|-----|-------|-----|
| **Die App** | `ghcr.io/real-life-org/rls-app` | `RLS_IMAGE_TAG` in der `.env` hochziehen, `docker compose up -d` |
| **Die Instanz-Vorlage** | `real-life-org/reallife-network-instanz` | `git fetch upstream && git merge upstream/main` |
| **Die Seite** | dieses Repo | `git pull` auf dem Server |

Dieses Repo ist ein Fork der Instanz-Vorlage. Antons Verbesserungen an Compose, Deploy und Vorlage holen wir uns über `upstream`; unsere Landingpage bleibt dabei unsere.

```bash
git remote add upstream https://github.com/real-life-org/reallife-network-instanz.git
git fetch upstream
git merge upstream/main
```

## Betrieb

```bash
docker compose up -d      # liest .env, zieht das gepinnte Image
```

Server: `/home/timo/apps/wir-ooo/` auf dem Strato-Host, Traefik mit Let's Encrypt davor.

## Mitarbeiten

Das Konzept liegt in [konzept/](konzept/) und ist der gemeinsame Stand. Wer etwas ändern will, öffnet ein Issue oder einen Pull Request.

Die Arbeit läuft in vier Wellen, siehe [konzept/04-pilot-und-umsetzung.md](konzept/04-pilot-und-umsetzung.md):

1. **Sichtbarkeit** Stiftungen und Projekte auf der Karte, mit Quelle und Prüfdatum
2. **Matching mit Begründung** jede Zeile zeigt, warum sie dort steht
3. **Menschen und Beiträge** reale Begegnung, Beitrag, später Gabe
4. **Der Kreis schließt sich** Anstifter, Bedarfe, Wirkung zurück auf die Karte

## Lizenz

Inhalte und Konzept: CC BY-SA 4.0. Der Real Life Stack steht unter seiner eigenen Lizenz.
