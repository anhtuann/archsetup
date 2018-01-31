from scripts import tools

#INSTALL
packages = ['syncthing',
            'syncthing-inotify',
            'syncthing-gtk']
tools.pacman(packages)

#CONFIGURATION
tools.bash_cmd('systemctl enable --now syncthing --user')

