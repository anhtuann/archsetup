import tools

#INSTALLATION
packages = ['xorg-server',
            'xorg-apps',
            'xorg-xinit',
            'arandr']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/machines/dreamland/confs/xinitrc_conf', '~/.xinitrc')