#!/bin/sh

echo "---- starting app ----"
exec "$@"

python -u /app/hermes.py app &
sleep 5
python -u /app/hermes.py cleanup