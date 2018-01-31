from scripts import tools

#INSTALL
packages = ['keepassxc',
            'pass',
            'rofi-pass']
tools.pacman(packages)

#CONFIGURATION
tools.stow('keepassxc')
