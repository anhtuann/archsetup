from scripts import tools

#INSTALL
packages = ['android-tools',
            'android-udev']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo usermod -aG adbusers $USER')
