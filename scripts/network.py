from scripts import tools

#INSTALL
packages = ['crda',
            'nmap',
            'networkmanager',
            'network-manager-applet',
            'gnome-keyring']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd("sudo sed -i '/FR/s/^#//g' /etc/conf.d/wireless-regdom")
