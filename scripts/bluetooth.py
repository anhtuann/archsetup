from scripts import tools

#INSTALL
packages = ['pulseaudio-alsa',
            'pulseaudio-bluetooth',
            'bluez',
            'bluez-libs',
            'bluez-utils',
            'blueman']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('sudo systemctl enable --now bluetooth.service')
tools.bash_cmd('gsettings set org.blueman.plugins.powermanager auto-power-on false')
tools.bash_cmd('sudo cp ~/Projects/archsetup/confs/bluetooth_rules /etc/polkit-1/rules.d/bluetooth.rules')
