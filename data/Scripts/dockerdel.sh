#!/bin/sh

LINES=$(tput lines)
COLUMNS=$(tput cols)

export NEWT_COLORS='
    root=white,black
    border=white,black
    title=white,black
    roottext=white,black
    window=white,black
    textbox=white,black
    button=black,white
    compactbutton=white,black
    listbox=white,black
    actlistbox=black,white
    actsellistbox=black,white
    checkbox=white,black
    actcheckbox=black,white
'

IMAGES=$(whiptail --checklist \
    "Image to delete" $LINES $COLUMNS $(( $LINES - 8 )) \
    $(docker image ls --format "{{ .Repository }}:{{.Tag}}" | xargs -I{} echo {} - OFF) \
    3>&1 1>&2 2>&3)

docker image rm $(echo "$IMAGES" | tr -d '"')
