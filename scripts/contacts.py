from scripts import tools

#INSTALL
packages = ['radicale',
            'python-passlib',
            'python-bcrypt',
            'apache-tools']
tools.pacman(packages)

#CONFIGURATION
tools.stow('radicale', sudo=True)
