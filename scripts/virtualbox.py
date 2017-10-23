import choices
from scripts import tools

#INSTALL
if choices.INSTALL_ENV == 'virtualbox':
    packages = ['virtualbox-guest-modules-arch',
                'virtualbox-guest-utils']
    tools.pacaur(packages)
else:
    packages = ['virtualbox', 
                'virtualbox-host-dkms', 
                'linux-headers',
                'virtualbox-guest-iso',
                'net-tools',
                'virtualbox-ext-oracle',
                'qt4']
    tools.pacaur(packages)
    tools.bash_cmd("sudo dkms install vboxhost/$(pacman -Q virtualbox|awk '{print $2}'|sed 's/\-.\+//') -k $(uname -rm|sed 's/\ /\//')")
    tools.bash_cmd("sudo gpasswd -a $USER vboxusers")
    
#CONFIGURATION
if choices.INSTALL_ENV != 'virtualbox':
    tools.stow('virtualbox', sudo=True)
