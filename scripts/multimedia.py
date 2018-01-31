from scripts import tools

#INSTALL
packages = ['mpv',
            'handbrake',
            'calibre',
            'audacity',
            'gimp',
            'gimp-plugin-gmic']
tools.pacman(packages)

#CONFIGURATION
tools.stow('mpv')
