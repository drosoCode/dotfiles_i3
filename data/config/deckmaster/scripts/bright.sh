#!/bin/bash

s=$(cat ~/.config/deckmaster/scripts/data/selectedscreen)
ddcutil -d $s setvcp 10 $1
