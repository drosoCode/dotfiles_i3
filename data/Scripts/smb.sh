#!/bin/bash

mount -t cifs //10.10.2.1/Share /mnt/kirito/share -o username=Thomas,workgroup=workgroup,iocharset=utf8
mount -t cifs //10.10.2.1/Homes /mnt/kirito/homes -o username=Thomas,workgroup=workgroup,iocharset=utf8
mount -t cifs //10.10.2.1/App /mnt/kirito/app -o username=Thomas,workgroup=workgroup,iocharset=utf8
