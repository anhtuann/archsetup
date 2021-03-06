from scripts import tools

#INSTALL
packages = ['zsh',
            'tmux']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd('chsh -s /bin/zsh')
with tools.cd('~/.config'):
    tools.git_clone('https://github.com/chriskempson/base16-shell.git')
command = 'sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"'
tools.bash_cmd('sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"')
tools.bash_cmd('rm ~/.zshrc')
tools.stow('zsh')
tools.link_conf('~/.config/base16-shell/scripts/base16-flat.sh', '~/.base16_theme')
