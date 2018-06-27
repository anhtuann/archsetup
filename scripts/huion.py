from scripts import tools

#INSTALL
packages = ['xf86-input-wacom',
            'linux-headers', #for digimend DKMS
            'digimend-kernel-drivers-dkms-git',
            'uclogic-tools']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('huion', sudo=True)
