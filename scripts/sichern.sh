#!/bin/sh
# Sichert, was nur auf dem Server existiert.
#
# Das ist wenig: Landing, Konfiguration und Compose liegen in Git, die Images
# sind aus Git neu baubar, und die Daten der Menschen liegen bei ihnen. Uebrig
# bleibt die `.env` mit acht Zeilen. Genau die fehlt bei einem Ausfall.
#
# Taeglich per Cron:
#   17 3 * * * /home/timo/apps/wir-ooo/scripts/sichern.sh

set -eu

INSTANZ="$(cd "$(dirname "$0")/.." && pwd)"
ZIEL="$HOME/sicherung"
STAND="$(date +%Y-%m-%d-%H%M)"
BEHALTEN=30

mkdir -p "$ZIEL"

ORDNER="$ZIEL/$STAND"
mkdir -p "$ORDNER"

# Die .env: die einzige Datei, die nur hier existiert.
[ -f "$INSTANZ/.env" ] && cp "$INSTANZ/.env" "$ORDNER/env"

# Alles, was im Instanz-Ordner liegt und nicht in Git steht. Meist nichts,
# manchmal ein Bild oder eine Sicherungskopie, die jemand abgelegt hat.
if command -v git >/dev/null 2>&1 && [ -d "$INSTANZ/.git" ]; then
  git -C "$INSTANZ" ls-files --others --exclude-standard | while read -r datei; do
    [ -f "$INSTANZ/$datei" ] || continue
    mkdir -p "$ORDNER/ungetrackt/$(dirname "$datei")"
    cp "$INSTANZ/$datei" "$ORDNER/ungetrackt/$datei"
  done
fi

# Welche Staende gab es? Ohne die Liste weiss beim Wiederaufbau niemand,
# welches Image zu welchem Commit gehoerte.
if command -v docker >/dev/null 2>&1; then
  docker images --format '{{.Repository}}:{{.Tag}} {{.CreatedAt}}' \
    | grep trustdonation > "$ORDNER/images.txt" 2>/dev/null || true
fi

# Die aeltesten Staende fallen, damit die Platte nicht volllaeuft.
ls -1d "$ZIEL"/*/ 2>/dev/null | sort | head -n -"$BEHALTEN" | while read -r alt; do
  rm -rf "$alt"
done

echo "$(date '+%Y-%m-%d %H:%M:%S') gesichert nach $ORDNER" >> "$ZIEL/log"
