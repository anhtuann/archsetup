from scripts import tools

#INSTALL
packages = ['mpv',
            'handbrake',
            'calibre',
            'audacity',
            'gimp',
            'gimp-plugin-gmic']
tools.pacaur(packages)

#CONFIGURATION
tools.mkdir('~/.config/mpv')
tools.link_conf('~/Projects/dotfiles/confs/mpv.conf', '~/.config/mpv/mpv.conf')
