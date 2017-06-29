from scripts import tools

#INSTALL
packages = ['firefox',
            'gstreamer',
            'gst-libav', 
            'gst-plugins-good']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/vimperatorrc_conf', '~/.vimperatorrc')
tools.link_conf('~/Projects/dotfiles/confs/firefox_desktop', '/usr/share/applications/firefox.desktop', sudo=True)
