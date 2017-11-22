from scripts import tools

#INSTALL
packages = ['deluge',
            'python2-service-identity',
            'aria2']
tools.pacaur(packages)

#CONFIGURATION
tools.stow(aria2)
tools.bash_cmd('touch ~/.aria2_input.conf')
