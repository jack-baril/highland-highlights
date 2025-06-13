#!/bin/sh

set -e

if [ -d 'highland-highlights' ]; then
  printf 'highland-highlights already exists.\n'
  printf '1) Replace the existing repository.\n'
  printf '2) Keep the existing repository.\n'
  printf 'Enter 1 or 2: '
  while true; do
    read input
    case "$input" in
      1)
        rm -rf highland-highlights
        git clone https://github.com/jack-baril/highland-highlights.git
        cd highland-highlights
        break
        ;;
      2)
        cd highland-highlights
        break
        ;;
      *)
        printf 'Error: Invalid input. Please enter 1 or 2.\n'
        ;;
    esac
  done
else
  git clone https://github.com/jack-baril/highland-highlights.git
  cd highland-highlights
fi

mkdir assets/documents

[ -d ".venv" ] || python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt

while true; do
  printf 'Please enter your API key from weatherapi.com: '
  read api_key
  if [ -z "$api_key" ]; then
    printf 'Error: Your API key cannot be empty. Please try again.\n'
    continue
  fi
  http_code=$(curl -s -o /dev/null -w "%http_code" \
    "http://api.weatherapi.com/v1/current.json?key=$api_key&q=gilbert")
  if [ "$http_code" -eq 200 ]; then
    printf 'WEATHER_API_KEY=%s\n' "$api_key" > .env
    break
  else
    printf 'Error: Your API key is invalid. Please try again.\n'
  fi
done

printf 'Success!\n'
printf 'Please refer back to the README for further instructions.\n'
