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
tools.bash_cmd('sudo systemctl enable --now bluetooth.service', shell=True)
tools.bash_cmd('gsettings set org.blueman.plugins.powermanager auto-power-on false', shell=True)
