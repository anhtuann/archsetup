from scripts import tools

#INSTALL
packages = ['cups',
            'hplip',
            'gtk3-print-backends']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo gpasswd -a anhtuann sys')
tools.bash_cmd('sudo gpasswd -a anhtuann lp')
tools.bash_cmd('sudo systemctl enable org.cups.cupsd.service')
tools.bash_cmd('sudo systemctl start org.cups.cupsd.service')
