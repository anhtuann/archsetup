from scripts import tools

#INSTALL
packages = ['libreoffice',
            'zathura',
            'zathura-pdf-mupdf']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('zathura')
