from scripts import tools

#INSTALL
packages = ['cronie']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo systemctl enable --now cronie')
