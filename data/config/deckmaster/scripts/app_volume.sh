#!/bin/bash

id=$(pactl list sink-inputs | grep "Sink Input" | cut -f 2 -d "#" | sed -n "${1}p")
#name=$(pactl list sink-inputs | grep "media.name" | cut -f 2 -d "\"" | sed -n "${1}p" | cut -c -10)
name=$(pactl list sink-inputs | grep "application.name" | cut -f 2 -d "\"" | sed -n "${1}p" | cut -c -10)
echo $id > /home/thomas/.config/deckmaster/scripts/data/vol_$1
echo $name
