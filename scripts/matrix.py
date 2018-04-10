from scripts import tools

#INSTALL
packages = ['matrix-synapse']
tools.pacman(packages)

#CONFIGURATION
tools.bash_cmd('sudo chmod 755 -R /var/lib/synapse')
tools.bash_cmd('sudo usermod -aG synapse anhtuann')
with tools.cd('/var/lib/synapse'):
    command = ['sudo -u synapse python2 -m synapse.app.homeserver']
    command.append('--server-name anhtuann.com')
    command.append('--config-path /etc/synapse/homeserver.yaml')
    command.append('--generate-config')
    command.append('--report-stats=yes')
    tools.bash_cmd(' '.join(command))
tools.bash_cmd('sudo systemctl enable --now synapse.service')
