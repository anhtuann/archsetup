from scripts import tools

#INSTALL
packages = ['zsh']
tools.pacaur(packages)

#CONFIGURATION
tools.bash_cmd(['chsh', '-s', '/bin/zsh'])
with tools.cd('~/.config'):
    tools.git_clone('https://github.com/chriskempson/base16-shell.git')
command = 'sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"'
tools.bash_cmd(command, shell=True)
tools.link_conf('~/Projects/dotfiles/confs/zshrc_conf', '~/.zshrc')

#may need to execute those two commands after reboot because of the change of shell
#another solution would be to use Popen which has an executable argument
tools.bash_cmd('source ~/.zshrc', shell=True)
tools.bash_cmd('base16_3024', shell=True)
