---
name: td-ausliefern
description: "Den trustdonation-Prototyp bauen und live bringen. Drei Tore lokal, Server-Build als trustdonation-app:proto-N, Umschalten der Instanz, Nachweis im Bundle. Mit den Fallen, die schon Zeit gekostet haben."
---

# Den Prototyp ausliefern

Vom Arbeitsstand zur laufenden App auf `trustdonation.org/app`.

**Repo:** `D:/Workspace/20-repos/rls-uebersicht`, Branch `trustdonation`, Remote `fork` = `lichtungooo/real-life-stack`
**Server:** `timo@h2980589.stratoserver.net` (Strato)
**Bauordner:** `~/build/td-app` · **Instanz:** `~/apps/wir-ooo` · **Container:** `rls-app-wir`
**Instanz-Repo:** `lichtungooo/trustdonation`, lokal `20-repos/trustdonation`

## 1. Alle Tore, lokal

```bash
cd /d/Workspace/20-repos/rls-uebersicht
python td-tools/pruefen.py
```

Sechs Tore in einem Befehl: Typen, Regeln, Naehte, Grenze, Budget, Gedaechtnis. **Voll fahren, nicht `--schnell`**: Der Schnelllauf ueberspringt Bau und Tests und hat schon zwei Fehler verdeckt.

Dazu der Augenschein: `pnpm dev:reference` auf **Port 5173**, niemals ausweichen. IndexedDB haengt am Origin.

Wer an der Oberflaeche gearbeitet hat, prueft zusaetzlich:

```bash
pnpm --filter reference exec vite preview --port 4173 &
python td-tools/zugang.py        # axe-core, null Funde erwartet
python td-tools/startlast.py     # Startlast, Budget 1200 KB
```

## 1a. Ein neues Paket? Dann den Dockerfile ergaenzen

Der Bau kopiert **jede `package.json` einzeln**, damit die Abhaengigkeits-Schicht im Cache bleibt:

```dockerfile
COPY packages/td-core/package.json packages/td-core/
COPY packages/td-ui/package.json packages/td-ui/
```

Fehlt ein Paket dort, installiert pnpm es nicht, und der Server-Bau bricht ab, sobald es etwas importiert. **Lokal faellt das nie auf**, weil dort alles installiert ist. Das hat einen Durchgang gekostet.

## 2. Musterdaten geaendert?

```bash
grep -n "SEED_VERSION = " packages/local-connector/src/local-connector.ts
```

Zahl um eins hoch, **immer wenn** sich Musterdaten geaendert haben. Ohne das sieht niemand die neuen Daten, der die App schon einmal offen hatte. Das ist dreimal passiert.

## 3. Commit und Push

```bash
git status --short        # PFLICHT, jedes Mal
git add <dateien>
git commit -m "..."
git status --short        # leer?
git push fork trustdonation
```

**Die Falle:** `git add`, danach weitere Korrekturen, dann `git commit` ohne erneutes `add`. Der Commit traegt den alten Stand, und der Server-Bau bricht mit einem Syntaxfehler ab, den es lokal nicht gibt.

Die `tsbuildinfo` gehoert nicht in den Commit:

```bash
git checkout -- apps/landing/tsconfig.tsbuildinfo
```

## 3a. Vorher sichern

```bash
ssh timo@h2980589.stratoserver.net "cd ~/apps/wir-ooo && sh scripts/sichern.sh"
```

Die `.env` ist die einzige Datei, die nur auf dem Server existiert, und sie aendert sich genau jetzt. Der Rest liegt in Git.

## 4. Server: holen und bauen

```bash
ssh timo@h2980589.stratoserver.net \
  "cd ~/build/td-app && git fetch origin trustdonation -q && git reset --hard origin/trustdonation -q && git log --oneline -1"

ssh timo@h2980589.stratoserver.net \
  "cd ~/build/td-app && docker build -f deploy/app/Dockerfile -t trustdonation-app:proto-N . 2>&1 | tail -4"
```

`N` ist die naechste freie Zahl. Vorhandene sehen:

```bash
ssh timo@h2980589.stratoserver.net "docker images --format '{{.Repository}}:{{.Tag}}' | grep trustdonation"
```

Der Bau dauert ein paar Minuten. Er endet mit `naming to docker.io/library/trustdonation-app:proto-N`.

## 5. Umschalten

```bash
ssh timo@h2980589.stratoserver.net \
  "cd ~/apps/wir-ooo && sed -i 's/^RLS_IMAGE_TAG=.*/RLS_IMAGE_TAG=proto-N/' .env && docker compose up -d 2>&1 | tail -3"
```

Die `.env` der Instanz:

| Variable | Wert |
|---|---|
| `RLS_DOMAIN` | `trustdonation.org` |
| `RLS_APP_NAME` | `trustdonation` |
| `RLS_RELAY_URL` | `wss://relay.web-of-trust.de` |
| `RLS_DEFAULT_CONNECTOR` | `local` (Musterdaten ohne Login) |
| `RLS_IMAGE` | `trustdonation-app` |
| `RLS_IMAGE_TAG` | `proto-N` |
| `RLS_HOME_SPACE_ID` | die Space-Id des Start-Netzwerks |
| `RLS_DOMAIN_ALT` | `wir.ooo` |

**Die Falle:** Eine Variable in der `.env` ist noch nicht im Container. Sie muss in der `environment`-Liste der `docker-compose.yml` stehen. Das liegt im Instanz-Repo `20-repos/trustdonation`, wird dort committet, gepusht und auf dem Server mit `git pull` geholt.

## 6. Nachweis

```bash
ssh timo@h2980589.stratoserver.net "docker ps --filter name=rls-app-wir --format '{{.Status}}'"
ssh timo@h2980589.stratoserver.net "docker exec rls-app-wir cat /usr/share/nginx/html/app/config.json"
curl -s -o /dev/null -w '%{http_code}\n' https://trustdonation.org/app/
```

Erwartet: `Up ... (healthy)`, eine vollstaendige `config.json`, `200`.

Und die Daten wirklich im Bundle, nicht nur im Repo:

```bash
ssh timo@h2980589.stratoserver.net \
  "docker exec rls-app-wir sh -c 'grep -o \"<eine-space-id>\" /usr/share/nginx/html/app/assets/*.js | wc -l'"
```

Umlaute im Bundle sind oft escaped. Nach **Ids** suchen, nicht nach Namen mit Umlaut.

## 7. Nachtragen

1. **`docs/AUSLIEFERUNGEN.md`**: neue Zeile oben mit Stand, Commit, Datum und dem, was ein Mensch merkt. Beim Zurueckdrehen zaehlt genau das.
2. **`memory/stand_trustdonation.md`**: Image-Tag, Commit, was unterwegs schiefging.
3. Bei einer neuen Falle zusaetzlich `40-forge/Real-Life-Forge/ERFAHRUNGEN.md`.

## Landing statt App

Die Landingpage liegt im Instanz-Repo und braucht keinen Image-Bau:

```bash
cd /d/Workspace/20-repos/trustdonation
# aendern, committen, pushen
ssh timo@h2980589.stratoserver.net "cd ~/apps/wir-ooo && git pull -q origin main"
```

Vor dem Push von JavaScript: `node --check landing/site.js`.

**Die Falle aus Erfahrung:** Ein unverankerter regulaerer Ausdruck hat einmal die halbe Navigation entfernt. Vor und nach einer Skript-Aenderung `wc -l` vergleichen, Ausdruecke mit `^` verankern.

## Zurueckdrehen

Der alte Tag liegt noch auf dem Server:

```bash
ssh timo@h2980589.stratoserver.net \
  "cd ~/apps/wir-ooo && sed -i 's/^RLS_IMAGE_TAG=.*/RLS_IMAGE_TAG=proto-<alt>/' .env && docker compose up -d"
```

Darum werden Images **nie geloescht**, solange der Platz reicht.

## Verwandt

- Skill `td-update` fuer Antons Aenderungen
- Skill `td-naht` bevor Antons Code angefasst wird
- `memory/reference_dns_trustdonation.md` fuer Domain und Zertifikat
- `memory/feedback_seed_version.md`
