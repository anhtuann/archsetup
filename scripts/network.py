from scripts import tools

#INSTALL
packages = ['crda']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd("sudo sed -i '/FR/s/^#//g' /etc/conf.d/wireless-regdom")
tools.mkdir('/etc/connman/', sudo=True)
tools.bash_cmd('sudo cp ~/Projects/dotfiles/confs/connman_conf /etc/connman/main.conf')
