from scripts import tools

#INSTALL
packages = ['android-tools',
            'android-udev']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo -v usermod -aG adbusers anhtuann')
