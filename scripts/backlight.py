from scripts import tools

#INSTALL
packages = ['acpilight',
            'xf86-video-intel']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('backlight', sudo=True)
tools.bash_cmd('sudo cp ~/Projects/archsetup/confs/backlight_rules /etc/udev/rules.d/90-backlight.rules')
tools.bash_cmd('sudo usermod -aG video anhtuann')
