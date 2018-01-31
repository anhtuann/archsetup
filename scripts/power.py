from scripts import tools

#INSTALL
packages = ['caffeine-ng',
            'xss-lock']
tools.pacman(packages)

#CONFIGURATION
tools.stow('logind', sudo=True)
