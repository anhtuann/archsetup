from scripts import tools

#INSTALL
packages = ['firefox',
            'gstreamer',
            'gst-libav', 
            'gst-plugins-good',
            'qutebrowser']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/vimperatorrc_conf', '~/.vimperatorrc')
tools.link_conf('~/Projects/dotfiles/confs/qutebrowser_conf', '~/.config/qutebrowser/qutebrowser.conf')
