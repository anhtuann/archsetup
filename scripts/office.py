from scripts import tools

#INSTALL
packages = ['libreoffice',
            'zathura',
            'zathura-pdf-mupdf']
tools.pacman(packages)

#CONFIGURATION
tools.stow('zathura')
