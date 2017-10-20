from scripts import tools

#INSTALL
packages = ['firefox',
            'gstreamer',
            'gst-libav', 
            'gst-plugins-good',
            'qutebrowser',
            'qt5-webengine',
            'qt5-webengine-widevine']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/vimperatorrc_conf', '~/.vimperatorrc')
tools.link_conf('~/Projects/dotfiles/confs/qutebrowser_config_py', '~/.config/qutebrowser/config.py')
