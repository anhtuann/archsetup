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
tools.stow('mpv')
