#!/bin/sh

set -e

cd highland-highlights
mkdir assets/documents

while true; do
  printf 'Please enter your API key from weatherapi.com: '
  read api_key
  if curl -s \
  "https://api.weatherapi.com/v1/current.json?key=${api_key}&q=gilbert" \
  | grep -q 'API key is invalid'; then
    printf 'Error: Your API key is invalid. Please try again.\n'
  else
    printf 'WEATHER_API_KEY=%s\n' "${api_key}" > .env
    break
  fi
done

python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt

printf 'Success!\nPlease refer back to the README for further instructions.\n'
