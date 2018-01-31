import choices
from scripts import tools

#INSTALL
if choices.INSTALL_ENV == 'virtualbox':
    packages = ['virtualbox-guest-modules-arch',
                'virtualbox-guest-utils']
    tools.pacman(packages)
else:
    packages = ['virtualbox',
                'virtualbox-host-modules-arch',
                'virtualbox-guest-iso',
                'net-tools',
                'virtualbox-ext-oracle']
    tools.pacman(packages)
    tools.bash_cmd("sudo gpasswd -a $USER vboxusers")
