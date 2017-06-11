import tools

#INSTALLATION
packages = ['vim']
tools.pacaur(packages)


#CONFIGURATION
tools.mkdir('.vim/bundle')
with tools.cd('.vim/bundle'):
    tools.git_clone('https://github.com/VundleVim/Vundle.vim.git', 'Vundle.vim')
    tools.bash_cmd(['vim', '+PluginInstall', '+qall'])
tools.link_conf('~/Projects/dotfiles/machines/dreamland/confs/vimrc_conf', '~/.vimrc')