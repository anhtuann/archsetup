from scripts import tools

packages = ['alsa-utils',
            'pulseaudio',
            'pulseaudio-alsa',
            'pavucontrol']
tools.pacman(packages)
