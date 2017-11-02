from scripts import tools

#INSTALL
packages = ['radicale',
            'python-passlib',
            'python-bcrypt',
            'apache-tools']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('radicale', sudo=True)
