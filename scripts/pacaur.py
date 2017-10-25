from scripts import tools
import glob

#INSTALL
packages = ['expac', 'yajl']
tools.pacman(packages)

tmp_folder = '/tmp/aur'
tools.mkdir(tmp_folder)

with tools.cd(tmp_folder):
    tools.git_clone('https://aur.archlinux.org/cower-git.git')
    tools.git_clone('https://aur.archlinux.org/pacaur.git')
    with tools.cd('cower-git'):
        tools.makepkg('*.pkg.tar.xz')
    with tools.cd('pacaur'):
        tools.makepkg('*.pkg.tar.xz')

#CONFIGURATION
tools.stow('pacaur')
