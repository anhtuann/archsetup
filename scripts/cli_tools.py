from scripts import tools

#INSTALL
packages = ['unrar',
            'unzip',
            'rsync',
            'ranger',
            'w3m']
tools.pacman(packages)

#CONFIGURATION
tools.bash_cmd('ranger --copy-config=all')
tools.stow('ranger')
