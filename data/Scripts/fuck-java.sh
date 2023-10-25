#!/bin/bash

PROC=$(pgrep java)
for p in $PROC; do renice -n 19 -p $p; done
