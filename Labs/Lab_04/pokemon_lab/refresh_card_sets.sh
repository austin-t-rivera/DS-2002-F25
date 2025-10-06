#!/usr/bin/env bash

echo "Refreshing all card sets in card_set_lookup/..."

# Loop through all .json files in the lookup directory
for FILE in card_set_lookup/*.json; do
    # Extract the SET_ID from the filename (e.g., base1-1.json becomes base1-1)
    SET_ID=$(basename "$FILE" .json)

    echo "Updating set: $SET_ID"

    # API call to get all cards for the set
    curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID&page=1&pageSize=250" > "$FILE"

    echo "Data written to "$FILE""
done

echo "All card sets refreshed."
