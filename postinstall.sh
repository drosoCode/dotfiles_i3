systemctl enable NetworkManager
systemctl enable ly
systemctl enable docker
su thomas
systemctl enable --user pipewire
systemctl enable --user mpd
xdg-settings set default-web-browser firefox.desktop
chsh -s /usr/bin/fish
