from scripts import tools

#INSTALL
packages = ['libreoffice',
            'zathura',
            'zathura-pdf-mupdf']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/zathura_conf', '~/.config/zathura/zathurarc')
