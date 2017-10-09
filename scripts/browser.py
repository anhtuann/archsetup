from scripts import tools

#INSTALL
packages = ['firefox',
            'gstreamer',
            'gst-libav', 
            'gst-plugins-good',
            'qutebrowser',
            'qt5-webengine']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/vimperatorrc_conf', '~/.vimperatorrc')
tools.link_conf('~/Projects/dotfiles/confs/qutebrowser_conf', '~/.config/qutebrowser/qutebrowser.conf')
tools.link_conf('~/Projects/dotfiles/confs/qutebrowser_keys_conf', '~/.config/qutebrowser/keys.conf')