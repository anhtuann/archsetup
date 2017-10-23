from scripts import tools

#INSTALL
packages = ['caffeine-ng',
            'xss-lock']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('logind', sudo=True)
