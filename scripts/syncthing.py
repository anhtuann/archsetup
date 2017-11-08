from scripts import tools

#INSTALL
packages = ['syncthing',
            'syncthing-inotify']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo systemctl enable --now syncthing@anhtuann.service')

