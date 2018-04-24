from scripts import tools

#INSTALL
tools.bash_cmd('gpg --recv-keys D1483FA6C3C07136') #Preparation for tor-browser
packages = ['keepassxc',
            'pass',
            'rofi-pass',
            'gnupg',
            'tor-browser']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('keepassxc')
tools.stow('rofi-pass')
