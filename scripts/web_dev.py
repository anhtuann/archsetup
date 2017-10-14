from scripts import tools

#INSTALL
packages = ['nginx-mainline',
            'google-chrome',
            'hugo']
tools.pacaur(packages)

#CONFIGURATION
tools.mkdir('/etc/nginx/sites-available', sudo = True)
tools.mkdir('/etc/nginx/sites-enabled', sudo = True)
tools.link_conf('~/Projects/dotfiles/confs/nginx_conf', '/etc/nginx/nginx.conf', sudo = True)
