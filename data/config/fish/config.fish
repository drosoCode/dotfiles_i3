if status is-interactive
    # Commands to run in interactive sessions can go here
end

function fish_greeting
end

abbr -g dc 'docker-compose'
abbr -g cpr 'rsync -rh --progress'
fish_add_path ~/.local/bin
abbr -g dhu '~/Android/Sdk/extras/google/auto/desktop-head-unit --config=~/Android/Sdk/extras/google/auto/config/default_sensors.ini'
abbr -g ytdl 'yt-dlp -f bestvideo+bestaudio --embed-chapters --embed-metadata --embed-thumbnail --embed-subs --no-cache-dir'
