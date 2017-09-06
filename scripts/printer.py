from scripts import tools

#INSTALL
packages = ['cups',
            'hplip',
            'gtk3-print-backends']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo gpasswd -a anhtuann sys', shell=True)
tools.bash_cmd('sudo gpasswd -a anhtuann lp', shell=True)
tools.bash_cmd('sudo systemctl enable org.cups.cupsd.service', shell=True)
tools.bash_cmd('sudo systemctl start org.cups.cupsd.service', shell=True)
