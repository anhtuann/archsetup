from scripts import tools

#INSTALL
packages = ['xf86-input-wacom',
            'linux-headers', #for digimend DKMS
            #'digimend-kernel-drivers-dkms-git', #support for H610P is not merged yet, pull request 114 is taking care of it
            'uclogic-tools']
tools.pacaur(packages)

#CONFIGURATION
tools.stow('huion', sudo=True)
tools.git_clone('https://github.com/DIGImend/digimend-kernel-drivers.git', '/tmp/digimend')
with tools.cd('/tmp/digimend'):
    tools.bash_cmd('git pull origin pull/114/head')
    tools.bash_cmd('make')
    tools.bash_cmd('sudo make install')
