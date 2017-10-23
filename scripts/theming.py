from scripts import tools

#INSTALL
packages = ['lxappearance',
            'ubuntu-themes',
            'qt5ct']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('gtk3')
tools.stow('qt5ct')
