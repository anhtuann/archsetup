from scripts import tools

#INSTALL
packages = ['xorg-xbacklight',
            'xf86-video-intel']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('backlight', sudo=True)
