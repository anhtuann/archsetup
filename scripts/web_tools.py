from scripts import tools

#INSTALL
packages = ['deluge',
            'python2-notify',
            'python2-mako',
            'python2-service-identity',
            'viber',
            'keepassxc',
            'rtv',
            'urlscan']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('deluge')
tools.stow('keepassxc')
tools.stow('rtv')
