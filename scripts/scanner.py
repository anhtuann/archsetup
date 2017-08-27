from scripts import tools

#INSTALL
packages = ['sane',
            'simple-scan',
            'brscan4']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo cp ~/Projects/dotfiles/confs/scanners_rules /usr/lib/udev/rules.d/49-sane-missing.rules', shell=True)
