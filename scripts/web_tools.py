from scripts import tools

#INSTALL
packages = ['aria2',
            'python2-notify',
            'python2-mako',
            'python2-service-identity',
            'viber',
            'keepassxc',
            'rtv',
            'urlscan']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('aria2')
tools.bash_cmd('touch ~/.aria2_input.conf')
tools.stow('keepassxc')
tools.stow('rtv')
