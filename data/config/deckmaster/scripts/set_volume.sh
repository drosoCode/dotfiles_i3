#!/bin/bash

if [[ $1 == "/" ]]; then
    id=$(cat ~/.config/deckmaster/scripts/data/vol_$2)
    pactl set-sink-input-mute $id toggle
else
    num=$(cat ~/.config/deckmaster/scripts/data/selected_vol_app)
    id=$(cat ~/.config/deckmaster/scripts/data/vol_$num)
    pactl set-sink-input-volume $id $1%
fi
