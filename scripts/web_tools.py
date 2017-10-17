from scripts import tools

#INSTALL
packages = ['dropbox',
            'deluge',
            'python2-notify',
            'python2-mako',
            'python2-service-identity',
            'viber',
            'keepassxc',
            'rtv',
            'urlscan']
tools.pacaur(packages)

#CONFIGURATION
tools.mkdir('~/.config/deluge')
tools.link_conf('~/Projects/dotfiles/confs/deluge_notifs_conf', '~/.config/deluge/notifications-gtk.conf')
tools.link_conf('~/Projects/dotfiles/confs/keepassxc_ini', '~/.config/keepassxc/keepassxc.ini')
tools.link_conf('~/Projects/dotfiles/confs/rtv_cfg', '~/.config/rtv/rtv.cfg')
tools.link_conf('~/Projects/dotfiles/confs/rtv_mailcap', '~/.mailcap')
