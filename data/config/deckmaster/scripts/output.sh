#!/bin/bash

# headphones / lineout
pactl set-sink-port alsa_output.pci-0000_0c_00.4.analog-stereo analog-output-$1
