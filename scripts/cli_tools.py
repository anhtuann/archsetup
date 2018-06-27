from scripts import tools

#INSTALL
packages = ['unrar',
            'unzip',
            'rsync',
            'ranger',
            'w3m',
            'pacman-contrib']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('ranger --copy-config=all')
tools.stow('ranger')
