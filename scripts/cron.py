from scripts import tools

#INSTALL
packages = ['cronie']
tools.pacman(packages)

#CONFIGURATION
tools.bash_cmd('sudo systemctl enable --now cronie')
