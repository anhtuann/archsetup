from scripts import tools

#INSTALL
packages = ['acpilight']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo cp ~/Projects/dotfiles/confs/backlight_rules /etc/udev/rules.d/90-backlight.rules')
tools.bash_cmd('sudo usermod -aG video anhtuann')
