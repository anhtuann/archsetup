from scripts import tools

#INSTALL
packages = ['cups',
            'hplip',
            'gtk3-print-backends']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo gpasswd -a $USER sys')
tools.bash_cmd('sudo gpasswd -a $USER lp')
tools.bash_cmd('sudo systemctl enable org.cups.cupsd.service')
tools.bash_cmd('sudo systemctl start org.cups.cupsd.service')
