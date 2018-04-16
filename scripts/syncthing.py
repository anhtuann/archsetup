from scripts import tools

#INSTALL
packages = ['syncthing',
            'syncthing-gtk']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('systemctl enable --now syncthing --user')

