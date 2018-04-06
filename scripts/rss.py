from scripts import tools

#INSTALL
packages = ['newsboat']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('newsboat')
