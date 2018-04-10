from scripts import tools

#INSTALL
packages = ['udisks2',
            'ntfs-3g',
            'dosfstools',
            'exfat-utils']
tools.pacman(packages)
