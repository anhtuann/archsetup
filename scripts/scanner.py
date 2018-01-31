from scripts import tools

#INSTALL
packages = ['sane',
            'simple-scan',
            'brscan4']
tools.pacman(packages)

#CONFIGURATION
tools.bash_cmd('sudo cp ~/Projects/dotfiles/confs/scanners_rules /etc/udev/rules.d/49-sane-missing.rules')
