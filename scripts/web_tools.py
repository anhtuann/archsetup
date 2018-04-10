from scripts import tools

#INSTALL
packages = ['aria2']
tools.pacman(packages)

#CONFIGURATION
tools.stow('aria2')
tools.bash_cmd('touch ~/.aria2_input.conf')
