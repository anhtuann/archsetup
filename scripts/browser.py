from scripts import tools

#INSTALL
packages = ['gstreamer',
            'gst-libav', 
            'gst-plugins-good',
            'qutebrowser',
            'qt5-webengine',
            'qt5-webengine-widevine',
            'firefox']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('qutebrowser')
