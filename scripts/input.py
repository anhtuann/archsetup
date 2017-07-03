from scripts import tools

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/libinput_conf', '/etc/X11/xorg.conf.d/30-touchpad.conf', sudo=True)
