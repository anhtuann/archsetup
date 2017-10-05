from scripts import tools

#INSTALL
packages = ['vim',
            'flake8']
tools.pacaur(packages)


#CONFIGURATION
tools.mkdir('~/.vim/bundle')
with tools.cd('~/.vim/bundle'):
    tools.git_clone('https://github.com/VundleVim/Vundle.vim.git', 'Vundle.vim')
tools.link_conf('~/Projects/dotfiles/confs/vimrc_conf', '~/.vimrc')
tools.link_conf('~/Projects/dotfiles/confs/flake8_conf', '~/.config/flake8')
tools.bash_cmd('vim -E -S ~/.vimrc +PluginInstall +qall')
tools.mkdir('/tmp/ycm_build')
with tools.cd('/tmp/ycm_build'):
    tools.bash_cmd('cmake -G "Unix Makefiles" . ~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp')
    tools.bash_cmd('cmake --build . --target ycm_core')
with tools.cd('~/.vim/bundle/YouCompleteMe'):
    tools.bash_cmd('git submodule update --init --recursive')
    tools.bash_cmd('python install.py --system-boost')
