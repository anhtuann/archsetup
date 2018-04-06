from scripts import tools

#INSTALL
packages = ['mpv',
            'handbrake',
            'calibre',
            'audacity',
            'youtube-viewer',
            'gtk2-perl',
            'perl-file-sharedir']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('mpv')
tools.stow('youtube-viewer')
