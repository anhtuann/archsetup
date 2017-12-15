from scripts import tools

#INSTALL
packages = ['acpilight']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo -v cp ~/Projects/dotfiles/confs/backlight_rules /etc/udev/rules.d/90-backlight.rules')
tools.bash_cmd('sudo -v usermod -aG video anhtuann')
