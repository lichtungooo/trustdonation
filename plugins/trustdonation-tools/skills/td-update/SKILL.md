---
name: td-update
description: "Antons Stand aus real-life-stack in den trustdonation-Prototyp holen. Neun Schritte mit drei Toren (Typen, Regeln, Augenschein), Naht-Pruefung, SEED_VERSION, Server-Build und Auslieferung. Enthaelt die bekannten Fallen mit ihren Loesungen."
---

# Antons Stand einspielen

Ein wiederholbarer Ablauf mit drei Toren. Er bricht ab, statt einen kaputten Stand auszuliefern.

**Wo:** Worktree `D:/Workspace/20-repos/rls-uebersicht`, Branch `trustdonation`.
**Remotes:** `origin` = `real-life-org/real-life-stack` (Anton), `fork` = `lichtungooo/real-life-stack` (wir).

## Vor dem Start

```bash
cd /d/Workspace/20-repos/rls-uebersicht
git remote -v                 # stimmt das Repo?
git rev-parse --abbrev-ref HEAD   # trustdonation?
git status --short            # sauber?
```

Ein unsauberer Baum wird **erst** aufgeraeumt. Ein Update auf ungespeicherter Arbeit ist der teuerste Weg, sie zu verlieren.

## Die neun Schritte

### 1. Antons Stand holen

```bash
git fetch origin master
git log --oneline HEAD..origin/master | head -30
git diff --stat HEAD..origin/master | tail -5
```

Lies die Commit-Titel. Sie sagen, was kommt.

### 2. Naehte zaehlen

Welche seiner Aenderungen treffen unsere Eintraege in `docs/NAEHTE.md`?

```bash
git diff --name-only HEAD..origin/master > /tmp/seine.txt
git diff --name-only <alter-basis-commit>..HEAD > /tmp/unsere.txt
comm -12 <(sort /tmp/seine.txt) <(sort /tmp/unsere.txt)
```

Jede Datei in der Schnittmenge wird ein Konflikt. Sind darunter Dateien, die **nicht** in `NAEHTE.md` stehen: erst eintragen, dann weitermachen. Eine unbenannte Naht ist ein Fehler im Register, nicht im Update.

### 3. Zusammenfuehren

```bash
git merge origin/master
```

Konflikte loesen. Leitlinie: **Antons Struktur behalten, unsere Arbeit daneben wieder einsetzen.** Nicht umgekehrt. Wer seine Umgestaltung zurueckdreht, um den eigenen Stand zu retten, zahlt beim naechsten Mal doppelt.

Bei jedem geloesten Konflikt fragen: *Gibt es dafuer inzwischen einen Haken?* Anton baut Register nach. Was gestern eine Naht war, ist heute vielleicht eine Schicht. Dann Skill `td-naht`, Frage 1.

### 4. Tor 1: Typen

```bash
pnpm install     # wenn er Abhaengigkeiten geaendert hat
pnpm build
```

**Falle:** `Cannot find module '@radix-ui/colors'` und Aehnliches heisst, dass eine neue Abhaengigkeit dazukam. `pnpm install` loest es.

### 5. Tor 2: Regeln

```bash
pnpm -r test
```

Alle acht Pakete gruen. Kein Tor wird uebersprungen: Ein gruener Build ohne gruene Tests sagt nichts ueber die Regeln, die wir geaendert haben.

**Falle:** Schlagen genau die Tests fehl, die wir in `NAEHTE.md` unter D eingetragen haben, hat Anton dort etwas geaendert. Erst verstehen, was er wollte, dann unsere Erweiterung darauf setzen.

### 6. Tor 3: Augenschein

```bash
pnpm dev:reference     # Port 5173, niemals ausweichen
```

Die fuenf Spaces stehen im Umschalter: Netzwerke (Marker & Maps, Real Life, trustdonation, Lichtung), Projekte (Marker & Maps, Lichtung), Stiftungen (Loewenherz Stiftung). Die Bereiche Netzwerk und Landingpage sind im Zahnrad da.

**Port 5173 ist fest.** IndexedDB haengt am Origin; ein anderer Port zeigt einen leeren Browser-Speicher.

### 7. Musterdaten

Haben sich Musterdaten geaendert, **eigene oder seine**:

```bash
grep -n "SEED_VERSION = " packages/local-connector/src/local-connector.ts
```

Zahl um eins hoch. Ohne das sieht niemand die neuen Daten, der die App schon einmal offen hatte. Das ist dreimal passiert, siehe `memory/feedback_seed_version.md`.

### 8. Bauen und ausliefern

```bash
git status --short          # PFLICHT vor jedem Push
git add <dateien>
git commit -m "..."
git push fork trustdonation
```

**Falle, die schon Zeit gekostet hat:** `git add`, danach weitere Korrekturen, dann `git commit` ohne erneutes `add`. Der Commit traegt den alten Stand, und der Server-Bau bricht ab. Darum `git status --short` vor jedem Push.

Auf dem Server:

```bash
ssh timo@h2980589.stratoserver.net
cd ~/build/td-app && git fetch origin trustdonation -q && git reset --hard origin/trustdonation -q
docker build -f deploy/app/Dockerfile -t trustdonation-app:proto-N .
cd ~/apps/wir-ooo && sed -i 's/^RLS_IMAGE_TAG=.*/RLS_IMAGE_TAG=proto-N/' .env
docker compose up -d
docker ps --filter name=rls-app-wir --format '{{.Status}}'
```

Pruefen, dass die Daten wirklich im Bundle sind:

```bash
docker exec rls-app-wir sh -c 'grep -o "<eine-space-id>" /usr/share/nginx/html/app/assets/*.js | wc -l'
```

**Falle:** Eine Variable in der `.env` ist noch nicht im Container. Sie muss in der `environment`-Liste der `docker-compose.yml` stehen. Das hat `RLS_HOME_SPACE_ID` einen Durchgang gekostet.

### 9. Nachtragen

1. `docs/NAEHTE.md`: Umfaenge neu messen, Zahlen oben nachziehen.
2. `memory/stand_trustdonation.md`: neuer Stand, Image-Tag, Commit, was unterwegs schiefging.
3. Bei einer neuen Falle: `40-forge/Real-Life-Forge/ERFAHRUNGEN.md`.

## Bekannte Fallen auf einen Blick

| Symptom | Ursache | Loesung |
|---|---|---|
| Neue Musterdaten erscheinen nicht | local-Connector laedt seinen gespeicherten Stand | `SEED_VERSION` hoch |
| Server-Bau bricht mit Syntaxfehler ab | Commit trug einen alten Dateistand | `git status --short` vor dem Push |
| `Cannot find module ...` | neue Abhaengigkeit von Anton | `pnpm install` |
| Ein Item fehlt in der Uebersicht | es liegt in zwei Spaces, der Connector laesst es dort weg | ein Item gehoert in genau einen Space |
| Konfiguration im Container leer | Variable fehlt in `environment` der Compose | dort ergaenzen, Instanz-Repo |
| `never[]` beim Bauen | leeres JSON-Array | Typ ausdruecklich nennen |

## Abbruch-Regeln

Halte an und frage, statt weiterzumachen, wenn:

- ein Konflikt in einer Datei auftritt, die **nicht** in `NAEHTE.md` steht,
- Tests fehlschlagen, die nichts mit unseren Naehten zu tun haben,
- Anton eine Datei geloescht oder umbenannt hat, an der eine Naht haengt,
- die Zahl der Naehte waechst, ohne dass ein Wunsch unterwegs ist.

Der Prototyp bleibt live auf dem alten Stand, bis das Update durch alle drei Tore ist.

## Verwandt

- `docs/ARCHITEKTUR.md` Teil 5 im Repo
- `docs/NAEHTE.md`
- Skill `td-naht`
- `memory/stand_trustdonation.md`
