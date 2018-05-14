from scripts import tools
import os

#INSTALL
packages = ['i3',
            'i3lock-color-git',
            'i3status',
            'py3status',
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
    tools.git_clone('gitsandman:anhtuann/useful-scripts.git')

#CONFIGURATION
tools.stow('i3')
tools.stow('i3status')
tools.stow('rofi')
tools.stow('polybar')
tools.stow('Xresources')
tools.stow('dunst')
tools.stow('redshift')
tools.stow('mimeapps')

screenshots_dir = '~/Pictures/screenshots'
tools.mkdir(screenshots_dir)
wallpapers_dir = '~/Pictures/wallpapers'
wallpaper = '~/Projects/archsetup/statics/takingcontrol.jpg'
wallpaper_lock = '~/Projects/archsetup/statics/takingcontrol_lock.png'
tools.mkdir(wallpapers_dir)
tools.bash_cmd('cp {} {}'.format(os.path.expanduser(wallpaper), os.path.expanduser(wallpapers_dir)))
tools.bash_cmd('cp {} {}'.format(os.path.expanduser(wallpaper_lock), os.path.expanduser(wallpapers_dir)))
tools.stow('fehbg')
