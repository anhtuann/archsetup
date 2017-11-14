from scripts import tools

#INSTALL
packages = ['tlp']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo systemctl enable --now tlp.service')
tools.bash_cmd('sudo systemctl enable --now tlp-sleep.service')
tools.bash_cmd('sudo systemctl mask --now systemd-rfkill.service')
tools.bash_cmd('sudo systemctl mask --now systemd-rfkill.socket')
