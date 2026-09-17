# Betrieb

Was laeuft wo, was passiert bei einem Ausfall, und was gesichert werden muss.

**Geprueft am 17.09.2026.**

---

## Was wo laeuft

| Teil | Ort | Quelle |
|---|---|---|
| Landingpage | `https://trustdonation.org` | dieses Repo, `landing/` |
| App | `https://trustdonation.org/app` | Image `trustdonation-app:proto-N` |
| Container | `rls-app-wir` auf dem Strato-Server | `docker-compose.yml` hier im Repo |
| Instanz-Konfiguration | `~/apps/wir-ooo/` auf dem Server | dieses Repo, per `git pull` |
| Bauordner der App | `~/build/td-app` auf dem Server | `lichtungooo/real-life-stack`, Branch `trustdonation` |
| Zertifikat | Traefik mit Let's Encrypt, TLS-ALPN-01 | automatisch |
| Identitaet und Daten der Menschen | ihre Geraete, synchronisiert ueber `relay.web-of-trust.de` | nicht bei uns |

Die letzte Zeile ist die wichtigste: **Wir halten keine Nutzerdaten.** Wer sich anmeldet, traegt seine Identitaet und seine Spaces auf dem eigenen Geraet; das Relay gleicht sie ab. Ein Ausfall unseres Servers nimmt niemandem seine Daten.

---

## Was ein Serverausfall kostet

| Was | verloren? | Wiederaufbau |
|---|---|---|
| Landingpage | nein | `git clone`, `git pull` |
| Instanz-Konfiguration (Compose, Branding) | nein | liegt in diesem Repo |
| App-Images (6 Staende, je 58 MB) | ja | neu bauen aus `lichtungooo/real-life-stack`, ein Befehl je Stand |
| `.env` der Instanz | **ja** | 304 Bytes, acht Zeilen, muss gesichert sein |
| Zertifikat | ja | Let's Encrypt stellt in ein bis zwei Minuten neu aus |
| Daten der Menschen | nein | liegen bei ihnen und im Relay |

**Der ganze Wiederaufbau dauert unter einer Stunde**, solange die `.env` da ist. Sie ist die einzige Datei, die nur auf dem Server existiert.

---

## Was gesichert wird

```bash
~/apps/wir-ooo/scripts/sichern.sh
```

Sichert die `.env` und alles, was im Instanz-Ordner nicht in Git liegt, nach `~/sicherung/` und haelt die letzten dreissig Staende. Laeuft taeglich per Cron:

```cron
17 3 * * * /home/timo/apps/wir-ooo/scripts/sichern.sh
```

Was **nicht** gesichert wird und warum:

- **Images**: jederzeit aus Git neu baubar, und 350 MB Sicherung fuer einen Befehl lohnt nicht.
- **Container-Zustand**: die App haelt nichts, was nicht aus Git oder von den Menschen kommt.
- **Zertifikate**: werden neu ausgestellt.

---

## Die Wacht

```bash
~/apps/wir-ooo/scripts/wacht.sh
```

Prueft alle fuenf Minuten, ob `trustdonation.org` und `/app` mit 200 antworten und ob der Container gesund ist. Meldet **nur bei einem Wechsel des Zustands**, nicht bei jedem Lauf: eine Nachricht alle fuenf Minuten wird nach einem Tag weggeblendet.

```cron
*/5 * * * * /home/timo/apps/wir-ooo/scripts/wacht.sh
```

Meldung per Telegram, wenn `TELEGRAM_TOKEN` und `TELEGRAM_CHAT` in der Umgebung stehen. Sonst steht alles im Log.

---

## Zurueckdrehen

Der vorige Stand liegt als Image bereit:

```bash
cd ~/apps/wir-ooo
sed -i 's/^RLS_IMAGE_TAG=.*/RLS_IMAGE_TAG=proto-<alt>/' .env
docker compose up -d
```

Darum werden **alte Images nie geloescht**, solange der Platz reicht. Am 17.09.2026: 23 GB von 290 GB belegt.

Was in welchem Stand steckt, steht in `docs/AUSLIEFERUNGEN.md` des Stack-Repos.

---

## Die Platten im Blick

```bash
df -h /
docker images --format '{{.Repository}}:{{.Tag}} {{.Size}}' | grep trustdonation
```

Wird es eng, fallen die aeltesten Prototyp-Images zuerst, nie der jeweils vorige.
