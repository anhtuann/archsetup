from scripts import tools

#INSTALL
packages = ['syncthing',
            'syncthing-inotify']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('systemctl enable --now syncthing --user')

