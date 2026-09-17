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

Sichert die `.env` und alles, was im Instanz-Ordner nicht in Git liegt, nach `~/sicherung/` und haelt die letzten dreissig Staende. Dazu die Liste der Images mit ihrem Datum: Ohne sie weiss beim Wiederaufbau niemand, welches Image zu welchem Commit gehoerte.

**Sie haengt an der Aenderung, nicht an der Uhr.** Die `.env` aendert sich genau dann, wenn ausgeliefert wird; ein taeglicher Lauf wuerde neunundzwanzig gleiche Staende erzeugen. Darum steht sie als Schritt im Ablauf `td-ausliefern` und wird zusaetzlich von Hand gefahren, wenn jemand etwas am Server aendert.

Was **nicht** gesichert wird und warum:

- **Images**: jederzeit aus Git neu baubar, und 350 MB Sicherung fuer einen Befehl lohnt nicht.
- **Container-Zustand**: die App haelt nichts, was nicht aus Git oder von den Menschen kommt.
- **Zertifikate**: werden in ein bis zwei Minuten neu ausgestellt.

## Die Wacht

**Von aussen**, als Arbeitsablauf in GitHub: `.github/workflows/wacht.yml`, alle fuenfzehn Minuten.

Von aussen ist besser als vom Server: Eine Pruefung, die auf demselben Rechner laeuft, schweigt genau dann, wenn der Rechner weg ist.

Sie prueft drei Dinge:

1. `https://trustdonation.org/` antwortet mit 200.
2. `https://trustdonation.org/app/` antwortet mit 200.
3. `app/config.json` ist da und vollstaendig. Ohne sie startet die App nicht, auch wenn die Seite laedt.

Bei einer Stoerung oeffnet der Lauf ein Issue mit dem Etikett `wacht` und haengt jeden weiteren Fund als Kommentar an. Ist wieder alles da, schreibt er die Entwarnung und schliesst es. **Eine Meldung je Stoerung**, nicht alle fuenfzehn Minuten eine.

Auf dem Server liegt zusaetzlich `scripts/wacht.sh`, das dieselbe Pruefung von innen macht und dabei auch den Zustand des Containers ansieht. Es laeuft von Hand oder aus einem Ablauf heraus; **fuer einen Zeitplan fehlt auf diesem Server der Dienst** (kein `cron`, und `systemd --user` ohne Linger stoppt beim Abmelden). Das ist kein Mangel, solange die Wacht von aussen laeuft.

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
