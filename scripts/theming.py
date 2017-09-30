from scripts import tools

#INSTALL
packages = ['lxappearance',
            'ubuntu-themes',
            'qt5ct']
tools.pacaur(packages)

#CONFIGURATION
tools.mkdir('~/.config/gtk-3.0')
tools.link_conf('~/Projects/dotfiles/confs/gtk3_ini', '~/.config/gtk-3.0/settings.ini')
tools.link_conf('~/Projects/dotfiles/confs/qt5ct_conf', '~/.config/qt5ct/qt5ct.conf')
