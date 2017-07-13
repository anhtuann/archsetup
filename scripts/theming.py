from scripts import tools

#INSTALL
packages = ['lxappearance',
            'ubuntu-themes']
tools.pacaur(packages)

#CONFIGURATION
tools.mkdir('~/.config/gtk-3.0')
tools.link_conf('~/Projects/dotfiles/confs/gtk3_ini', '~/.config/gtk-3.0/settings.ini')
