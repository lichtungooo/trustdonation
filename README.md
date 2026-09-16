# trustdonation

**Infrastruktur für vertrauensbasierte Förderung**

Stiftungen, Projekte, Anstifter, Zustifter und ihre Community finden auf einer Karte zueinander. Weltweit. Getragen vom Kollektiv Lichtung e.V., gebaut auf dem [Real Life Stack][rls], Vertrauen über das [Web of Trust][wot].

> trustdonation baut eine Infrastruktur, mit der Stiftungen ihre Förderwirkung erhöhen, weil passende Projekte, Menschen, Anstifter und Zustifter leichter zusammenfinden.

| | |
|---|---|
| Domain | trustdonation.org *(DNS in Arbeit)* |
| Baustelle | <https://wir.ooo> |
| Konzept | [docs/README.md](docs/README.md) |
| Für Agenten | [AGENTS.md](AGENTS.md), [llms.txt](llms.txt) |

---

## Das Problem

- **Gute Projekte** finden die Förderer nicht, die zu ihnen passen.
- **Förderer** sehen die passenden Projekte nicht, und Mittel bleiben liegen.
- **Die Community** weiß nicht, wo sie in ihrer Nähe beitragen kann.
- **Stiftungen** finden keinen Nachwuchs für ihre Gremien.
- **Zustifter** wissen nicht, wo ihr Kapital dauerhaft wirkt.

Verzeichnisse lösen einen Teil davon: Sie listen Stiftungen. Was fehlt, ist die Verbindung zwischen Liste und Wirklichkeit.

## Die Lösung

- **Karte** mit Stiftungen, Projekten und Community, weltweit, jeder Eintrag mit Quelle und Prüfdatum
- **Matching** mit Begründung Zeile für Zeile, nie als Note
- **Projektseite**, die zeigt, was ein Projekt tut, braucht und schon erreicht hat
- **Vertrauensschicht** aus realer Begegnung, bestätigtem Beitrag und gewachsenem Vertrauen

Geld steht nicht am Anfang. Es ist ein Ergebnis einer Beziehung.

```text
Vertrauen → Entdeckung → Matching → Verbindung → Finanzierung → Umsetzung → Wirkung
```

---

## Architektur

```text
┌────────────────────────────────────────────────────────────┐
│  trustdonation                                             │
│  Landingpage · Stiftungsdaten · Matching · Ansprache       │
├────────────────────────────────────────────────────────────┤
│  Real Life Stack (RLS)                                     │
│  App Shell · Karte · Gruppen · Profile · Kalender · Feed   │
├────────────────────────────────────────────────────────────┤
│  Web of Trust (WoT)                                        │
│  Identität · Begegnung · Bestätigung · Sync                │
└────────────────────────────────────────────────────────────┘
```

trustdonation ist eine **Instanz** des Real Life Stack, kein Fork. Die App kommt als fertiges Image, dieses Repo hält Konfiguration und Inhalt (siehe [Spec 11 des Stacks][spec11]).

Wer die drei Namen auseinanderhalten will: [docs/00-ueberblick.md → Abgrenzung der Namen](docs/00-ueberblick.md).

---

## Die vier Grundsätze

1. **Geld kauft keine Vertrauensbewertung.** Partner bekommen Status und Mitsprache, keine bessere Platzierung im Matching.
2. **Fakten statt Noten.** Kriterien, Quelle, Prüfdatum. Keine Sterne, keine Ampeln, keine Bewertung von Organisationen.
3. **Vertrauen entsteht im Netz, nicht bei uns.** Wir stellen kein Zertifikat aus.
4. **Die Identität bleibt beim Menschen.** Schlüssel auf dem Gerät, Profil wandert mit.

---

## Was hier liegt

```text
docs/           das Konzept, normativ
  fragen/       Fragebögen für Projekt, Stiftung, Gespräch, plus gelöste Beispiele
  glossar.md    Begriffe
landing/        die Landingpage, freies HTML, kein Build
  stile/        neun Sprachstile als Wörterbuch, je eine JSON-Datei
  logo/         Wortmarke und Signet
  fonts/        selbst gehostet, keine Anfrage an Dritte
branding/       theme.json (Farbtokens) und favicon.svg für die App
docker-compose.yml
.env.example    Vorlage; die echte .env steht auf dem Server
AGENTS.md       Regeln für Agenten und Menschen
llms.txt        maschinenlesbarer Überblick
```

---

## Drei Arten von Updates

| Was | Woher | Wie |
|---|---|---|
| **Die App** | `ghcr.io/real-life-org/rls-app` | `RLS_IMAGE_TAG` in der `.env` hochziehen, `docker compose up -d` |
| **Die Instanz-Vorlage** | [reallife-network-instanz][vorlage] | `git fetch upstream && git merge upstream/main` |
| **Die Seite** | dieses Repo | `git pull` auf dem Server |

Dieses Repo ist ein Fork der Instanz-Vorlage. Verbesserungen an Compose, Deploy und Vorlage holen wir uns über `upstream`, unsere Landingpage bleibt dabei unsere.

```bash
git remote add upstream https://github.com/real-life-org/reallife-network-instanz.git
git fetch upstream && git merge upstream/main
```

---

## Betrieb

```bash
cp .env.example .env      # Domain, Name, Image-Tag eintragen
docker compose up -d      # zieht das gepinnte Image
```

Die Compose-Datei trägt zwei Domains: `RLS_DOMAIN` und `RLS_DOMAIN_ALT`. So laufen Zieldomain und Baustelle auf demselben Container.

Server: `/home/timo/apps/wir-ooo/`, Traefik mit Let's Encrypt davor.

---

## Mitarbeiten

Das Konzept in [docs/](docs/) ist der gemeinsame Stand. Wer etwas ändern will, öffnet ein Issue oder einen Pull Request. Bei Konflikt zwischen Konzept und Umsetzung gewinnt das Konzept.

Die Arbeit läuft in vier Wellen ([docs/07-pilot.md](docs/07-pilot.md)):

1. **Sichtbarkeit** Stiftungen und Projekte auf der Karte, mit Quelle und Prüfdatum
2. **Matching mit Begründung** jede Zeile zeigt, warum sie dort steht
3. **Menschen und Beiträge** reale Begegnung, Beitrag, später Gabe
4. **Der Kreis schließt sich** Anstifter, Bedarfe, Wirkung zurück auf die Karte

Wer mit einer Stiftung spricht, nimmt [docs/fragen/stiftungsgespraech.md](docs/fragen/stiftungsgespraech.md) mit. Wer ein Projekt anlegt, geht [docs/fragen/projekt.md](docs/fragen/projekt.md) durch. Zwei gelöste Beispiele zeigen, wie ein fertiger Durchlauf aussieht.

---

## Lizenz

Konzept und Inhalte: CC BY-SA 4.0. Der Real Life Stack steht unter seiner eigenen Lizenz.

[rls]: https://github.com/real-life-org/real-life-stack
[wot]: https://github.com/antontranelis/web-of-trust
[vorlage]: https://github.com/real-life-org/reallife-network-instanz
[spec11]: https://github.com/real-life-org/real-life-stack/blob/master/docs/spec/11-runtime-config-und-branding.md
