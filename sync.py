#!/sbin/python

import argparse
import os
import pathlib
import re

# config:
# pc_loc, git_loc, files
DATA_DIR = "./data/"
files = [
    [
        "~/.config",
        DATA_DIR+"config",
        [
            "alacritty/",
            "cava/config",
            "Code/User/settings.json",
            "discord/settings.json",
            "dunst/",
            "fish/config.fish",
            "gtk-3.0/settings.ini",
            "i3/",
            "i3status-rust/",
            "mpd/mpd.conf",
            "ncmpcpp/config",
            "picom/picom.conf",
            "rofi/",
        ],
    ],
    [
        "/etc",
        DATA_DIR+"etc",
        [
            "X11/xorg.conf.d/",
            "minidlna.conf",
            "pacman.conf",
            "environment",
            "docker/daemon.json",
            "ly/config.ini",
        ],
    ],
    ["~", DATA_DIR, ["Scripts/"]],
]

# dotfiles functions

def exec(command):
    print(f"\033[94m{command}\033[0m")
    os.system(command)

def backup_vsc():
    exec(f"code --list-extensions > ./vsc_ext")

def install_vsc():
    with open("./vsc_ext", "r") as f:
        for ext in f.readlines():
            exec(f"code --install-extension {ext}")

def backup_pkg():
    exec(f"python ~/Scripts/list_installed.py > ./packages")

def install_pkg():
    with open("./packages", "r") as f:
        pkgs = " ".join(f.readlines())
        exec(f"yay -Syu {pkgs}")

def br_files(cfg, backup=True):
    for i in cfg:
        for f in i[2]:
            from_path = os.path.join(i[int(not backup)], f)
            to_path = os.path.join(i[int(backup)], f)
            if not backup and not os.path.exists(os.path.dirname(from_path)):
                os.makedirs(os.path.dirname(from_path))
            if backup and not os.path.exists(os.path.dirname(to_path)):
                os.makedirs(os.path.dirname(to_path))
            #  -v --info=progress2
            exec(
                f"rsync -a --delete {from_path} {to_path}"
            )

def check_secrets(path):
    foundSecrets = False
    reg = re.compile("[_\-\w]+((key)|(secret)|(password)|(token)){1}.*[= :]{1}", re.IGNORECASE)
    for f in pathlib.Path(path).rglob("*"):
        if not f.is_dir():
            with open(f, "r") as file:
                matchedLines = []
                for l in file.readlines():
                    if reg.search(l) is not None:
                        matchedLines.append(l)
                if matchedLines != []:
                    foundSecrets = True
                    print(f"\033[96m-------- {f} :\033[0m")
                    for x in matchedLines:
                        print(x.strip("\n"))
    return foundSecrets

# arg parsing

parser = argparse.ArgumentParser(description="Dotfiles Sync")
parser.add_argument(
    "--backup-conf", action="store_true", help="backup config files", default=False
)
parser.add_argument(
    "--backup-packages",
    action="store_true",
    help="backup installed packages list",
    default=False,
)
parser.add_argument(
    "--backup-ext",
    action="store_true",
    help="backup installed vscode extensions",
    default=False,
)
parser.add_argument(
    "--install-packages", action="store_true", help="install packages", default=False
)
parser.add_argument(
    "--install-ext",
    action="store_true",
    help="install vscode extensions",
    default=False,
)
parser.add_argument(
    "--install-conf", action="store_true", help="install config files", default=False
)
parser.add_argument(
    "--check", action="store_true", help="check for secrets in backup conf files", default=False
)
parser.add_argument(
    "--install", action="store_true", help="install and configure system", default=False
)
parser.add_argument(
    "--backup", action="store_true", help="backup install and conf", default=False
)
args = parser.parse_args()

if args.backup or args.backup_conf:
    br_files(files, True)
if args.backup or args.backup_ext:
    backup_vsc()
if args.backup or args.backup_packages:
    backup_pkg()

if args.install or args.install_conf:
    br_files(files, False)
if args.install or args.install_packages:
    install_pkg()
if args.install or args.install_ext:
    install_vsc()

if args.check:
    print("\033[93m============= SECRETS CHECK =============\033[0m\n")
    if check_secrets(DATA_DIR):
        exit(1)
elif args.backup or args.backup_conf:
    print("\n\n\033[93m============= SECRETS CHECK =============\033[0m\n")
    check_secrets(DATA_DIR)
