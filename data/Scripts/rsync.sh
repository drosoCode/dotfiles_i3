date
export RSYNC_PASSWORD=xxxx
rsync -av rsync://Backup@10.10.2.1/Musique/ ~/Music
mpc rescan
