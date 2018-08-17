from scripts import tools

#INSTALL
packages = ['libreoffice',
            'zathura',
            'zathura-pdf-poppler']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('zathura')
