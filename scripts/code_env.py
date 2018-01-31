from scripts import tools

#INSTALL
packages = ['python',
            'python-virtualenv',
            'python-virtualenvwrapper',
            'tk',
            'cmake', #installed to build YouCompleteMe vim Plugin
            'boost', #same as cmake for YouCompleteMe
            'python-opengl'] #for qutebrowser with webengine backend
tools.pacman(packages)
