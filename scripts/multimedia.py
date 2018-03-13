from scripts import tools

#INSTALL
packages = ['mpv',
            'handbrake',
            'calibre',
            'audacity',
            'gimp',
            'gimp-plugin-gmic',
            'blender']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('mpv')
