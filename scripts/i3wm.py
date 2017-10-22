from scripts import tools
import os

#INSTALL
packages = ['i3',
            'rxvt-unicode',
            'rofi',
            'scrot',
            'feh',
            'imagemagick',
            'ghostscript',
            'dunst',
            'thunar',
            'thunar-volman',
            'thunar-archive-plugin',
            'file-roller',
            'gvfs',
            'tumbler',
            'xclip',
            'redshift']
tools.pacaur(packages)

with tools.cd('~/Projects/'):
    tools.git_clone('git@anhtuann.com:anhtuann/useful-scripts.git')

#CONFIGURATION
tools.mkdir('~/.config/i3')
tools.mkdir('~/.config/i3status')
tools.mkdir('~/.config/dunst')
tools.link_conf('~/Projects/dotfiles/confs/i3_conf', '~/.config/i3/config')
tools.link_conf('~/Projects/dotfiles/confs/i3status_conf', '~/.config/i3status/config')
tools.link_conf('~/Projects/dotfiles/confs/Xresources_conf', '~/.Xresources')
tools.link_conf('~/Projects/dotfiles/confs/dunst_conf', '~/.config/dunst/dunstrc')
tools.link_conf('~/Projects/dotfiles/confs/redshift_conf', '~/.config/redshift.conf')
tools.link_conf('~/Projects/dotfiles/confs/mimeapps_list', '~/.config/mimeapps.list')

screenshots_dir = '~/Pictures/screenshots'
tools.mkdir(screenshots_dir)
wallpapers_dir = '~/Pictures/wallpapers'
wallpaper = '~/Projects/dotfiles/statics/takingcontrol.jpg'
tools.mkdir(wallpapers_dir)
tools.bash_cmd('cp {} {}'.format(os.path.expanduser(wallpaper), os.path.expanduser(wallpapers_dir)))
tools.link_conf('~/Projects/dotfiles/confs/fehbg_conf','~/.fehbg')

