from scripts import tools

#INSTALL
packages = ['vim']
tools.pacman(packages)


#CONFIGURATION
tools.mkdir('~/.vim/bundle')
with tools.cd('~/.vim/bundle'):
    tools.git_clone('https://github.com/VundleVim/Vundle.vim.git', 'Vundle.vim')
tools.stow('vim')
tools.stow('flake8')
tools.bash_cmd('vim -E -S ~/.vimrc +PluginInstall +qall')
