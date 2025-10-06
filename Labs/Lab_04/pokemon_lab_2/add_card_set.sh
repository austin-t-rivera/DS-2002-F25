#!/usr/bin/env bash

# Prompt user for the TCG set ID
read -r -p "Enter the TCG Card Set ID (e.g., base1, base4): " SET_ID

if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

echo "Fetching data for set: $SET_ID..."

# API call to get all cards in the set
curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID&page=1&pageSize=250" > card_set_lookup/"$SET_ID".json

echo "Successfully saved data to card_set_lookup/$SET_ID.json"
