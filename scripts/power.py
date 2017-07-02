from scripts import tools

#INSTALL
packages = ['caffeine-ng',
            'xss-lock']
tools.pacaur(packages)

#CONFIGURATION
tools.link_conf('~/Projects/dotfiles/confs/logind_conf', '/etc/systemd/logind.conf', sudo=True)
