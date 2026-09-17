#!/bin/sh
# Sieht nach, ob trustdonation.org erreichbar ist, und meldet sich, wenn nicht.
#
# Faellt die Seite waehrend eines Stiftungsgespraechs aus, kostet das mehr als
# jede Funktion bringt. Bisher haetten wir es durch einen Anruf erfahren.
#
# Laeuft auf dem Server als Cron-Eintrag, alle fuenf Minuten:
#   */5 * * * * /home/timo/apps/wir-ooo/scripts/wacht.sh
#
# Meldet nur bei einem Wechsel des Zustands, nicht bei jedem Lauf: eine
# Nachricht alle fuenf Minuten wird nach einem Tag weggeblendet.

set -u

ZIELE="https://trustdonation.org/ https://trustdonation.org/app/"
MERKER=/tmp/trustdonation-wacht.zustand
LOG=/var/log/trustdonation-wacht.log
[ -w /var/log ] || LOG="$HOME/trustdonation-wacht.log"

jetzt() { date "+%Y-%m-%d %H:%M:%S"; }

melden() {
  # Telegram, wenn hinterlegt. Sonst bleibt es im Log.
  if [ -n "${TELEGRAM_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT:-}" ]; then
    curl -s -o /dev/null --max-time 10 \
      "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" \
      --data-urlencode "chat_id=${TELEGRAM_CHAT}" \
      --data-urlencode "text=$1"
  fi
  echo "$(jetzt) $1" >> "$LOG"
}

fehler=""
for ziel in $ZIELE; do
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "$ziel")
  [ "$code" = "200" ] || fehler="${fehler}${ziel} antwortet ${code}. "
done

# Zusaetzlich: laeuft der Container, und ist er gesund?
if command -v docker >/dev/null 2>&1; then
  zustand=$(docker inspect -f '{{.State.Health.Status}}' rls-app-wir 2>/dev/null || echo "fehlt")
  [ "$zustand" = "healthy" ] || fehler="${fehler}Container rls-app-wir: ${zustand}. "
fi

vorher=$(cat "$MERKER" 2>/dev/null || echo "gut")

if [ -n "$fehler" ]; then
  jetzt_zustand="schlecht"
  [ "$vorher" = "schlecht" ] || melden "trustdonation ist gestoert: $fehler"
else
  jetzt_zustand="gut"
  [ "$vorher" = "gut" ] || melden "trustdonation ist wieder erreichbar."
fi

echo "$jetzt_zustand" > "$MERKER"
[ "$jetzt_zustand" = "gut" ]
