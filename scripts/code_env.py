from scripts import tools

#INSTALL
packages = ['python',
            'python-virtualenv',
            'python-virtualenvwrapper',
            'tk',
            'cmake', #installed to build YouCompleteMe vim Plugin
            'boost', #same as cmake for YouCompleteMe
            'lua', #for weechat
            'lua-cjson']  #for weechat
tools.pacman(packages)
