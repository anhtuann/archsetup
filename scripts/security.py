from scripts import tools

#INSTALL
packages = ['keepassxc',
            'pass',
            'rofi-pass']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('keepassxc')
tools.stow('rofi-pass')
