#!/bin/bash

if [[ $2 == "dup" ]]
then
    xrandr --output eDP1 --auto --output ${1:-DP1} --scale 1.5x1.7777 --same-as eDP1 ${@:3}
    # [2880/1920]x[1920/1080] 2880x1920 -> 1920x1080
else
    xrandr --output eDP1 --auto --output ${1:-DP1} --auto --scale 2x2 --right-of eDP1 ${@:2}
fi

sh ~/.fehbg

#xrandr --output eDP-1 --auto --output DP-1 --auto --scale 2x2 --right-of eDP-1
#xrandr --output eDP1 --scale 0.5x0.5 --output DP2 --right-of eDP1 --output HDMI1 --right-of DP2
#xrandr --output HDMI --scale [2880/1920]x[1920/1080] # 2880x1920 -> 1920x1080
