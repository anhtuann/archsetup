from scripts import tools

#INSTALL
packages = ['libmtp',
            'android-file-transfer',
            'udisks2',
            'udiskie',
            'udiskie-dmenu-git',
            'ntfs-3g',
            'dosfstools',
            'hfsprogs',
            'exfat-utils',
            'gparted']
tools.pacaur(packages)
