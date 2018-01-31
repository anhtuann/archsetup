from scripts import tools

#INSTALL
packages = ['xorg-server',
            'xorg-apps',
            'xorg-xinit',
            'arandr',
            'xbanish']
tools.pacman(packages)

#CONFIGURATION
tools.stow('xinit')

