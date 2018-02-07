from scripts import tools

#INSTALL
packages = ['crda',
            'nmap']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd("sudo sed -i '/FR/s/^#//g' /etc/conf.d/wireless-regdom")
tools.stow('connman', sudo=True)
