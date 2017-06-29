from scripts import tools

#INSTALL
packages = ['acpilight']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/backlight_rules', '/etc/udev/rules.d/90-backlight.rules', sudo=True)
tools.bash_cmd('sudo usermod -aG video anhtuann', shell=True)
