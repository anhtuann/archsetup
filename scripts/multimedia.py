from scripts import tools

#INSTALL
packages = ['mpv',
            'handbrake',
            'calibre',
            'audacity']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('mpv')
