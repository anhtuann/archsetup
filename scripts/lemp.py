from scripts import tools

#INSTALL
packages = ['nginx-mainline',
            'php',
            'php-fpm',
            'mariadb']
tools.pacman(packages)

#CONFIGURATION
tools.mkdir('/etc/nginx/sites-available', sudo=True)
tools.mkdir('/etc/nginx/sites-enabled', sudo=True)
tools.stow('nginx', sudo=True)
tools.stow('php', sudo=True)
tools.bash_cmd('sudo systemctl enable --now nginx.service')
tools.bash_cmd('sudo systemctl enable --now php-fpm.service')
tools.bash_cmd('sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql')
tools.bash_cmd('sudo mysql_secure_installation')
