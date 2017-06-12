from scripts import tools

#INSTALL
packages = ['zsh']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd(['rm', '~/.zshrc'])
tools.link_conf('~/Projects/dotfiles/confs/zshrc_conf', '~/.zshrc')
with tools.cd('~/.config'):
    tools.git_clone('https://github.com/chriskempson/base16-shell.git')
command = 'sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"'
tools.bash_cmd(command, shell=True)
tools.bash_cmd('source ~/.zshrc', shell=True)
tools.bash_cmd('base16_3024', shell=True)
