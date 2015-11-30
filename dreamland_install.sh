#sort mirrors by speed
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo sh -c 'rankmirrors -n 5 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirrorlist'
sudo pacman -Syu

#graphic drivers
sudo pacman -S --noconfirm nvidia bumblebee 
gpasswd -a anhtuann bumblebee
sudo systemctl enable bumblebeed.service

#Xserver
sudo pacman -S --noconfirm xorg-server xorg-server-utils xorg-apps
sudo pacman -S --noconfirm xorg-xinit

#i3 initialisation
sudo pacman -S --noconfirm i3
echo exec i3 > ~/.xinitrc

#git for pacaur install
sudo pacman -S --noconfirm git
git config --global push.default simple
sed -i '1s/^/eval $(ssh-agent)\n/' ~/.xinitrc

#pacaur install
mkdir /tmp/aur
cd /tmp/aur
git clone http://aur.archlinux.org/cower.git
git clone http://aur.archlinux.org/pacaur.git
gpg --recv-keys 1EB2638FF56C0C53
cd cower
makepkg -s
sudo pacman -U cower*.pkg.tar.xz
cd ../pacaur
makepkg -s
sudo pacman -U pacaur*.pkg.tar.xz
cd

#various applications for i3+firefox
pacaur -S --noconfirm rxvt-unicode
pacaur -S --noconfirm xf86-input-libinput 
pacaur -S --noconfirm ttf-hack
pacaur -S --noconfirm firefox
pacaur -S --noconfirm xbacklight kbdlight

#dotfiles downloaded from github
mkdir ~/Projects 
cd ~/Projects
git clone https://github.com/anhtuann/dotfiles.git

#useful scripts downloaded from github
git clone https://github.com/anhtuann/useful-scripts.git

#vim
pacaur -S --noconfirm vim
ln -sf ~/Projects/dotfiles/dreamland/vim/vimrc ~/.vimrc

#Xresources and bashrc added
git clone https://github.com/chriskempson/base16-shell.git ~/.config/base16-shell
ln -sf ~/Projects/dotfiles/dreamland/bash/bashrc ~/.bashrc
ln -sf ~/Projects/dotfiles/dreamland/Xresources/Xresources ~/.Xresources
source ~/.bashrc

#i3 config added
mkdir ~/.i3
ln -sf ~/Projects/dotfiles/dreamland/i3/i3_config ~/.i3/config
pacaur -S --noconfirm rofi scrot playerctl feh volumeicon dunst
mkdir -p ~/.config/i3status
ln -sf ~/Projects/dotfiles/dreamland/i3/i3status_config ~/.config/i3status/config

#various utilities
pacaur -S --noconfirm alsa-utils
pacaur -S --noconfirm xclip
pacaur -S --noconfirm transmission-cli
pacaur -S --noconfirm imagemagick
pacaur -S --noconfirm ttf-mplus
pacaur -S --noconfirm unrar

#ssh keys
pacaur -S --noconfirm openssh
ssh-keygen
echo 'eval $(ssh-agent)' >> ~/.xinitrc

#vimperator
ln -sf ~/Projects/dotfiles/dreamland/vimperator/vimperatorrc ~/.vimperatorrc

#mtp support
pacaur -S --noconfirm libmtp android-file-transfer

#multimedia
pacaur -S --noconfirm mpv
pacaur -S --noconfirm gstreamer gst-libav gst-plugins-good

#coding
pacaur -S --noconfirm python python-virtualenv python-virtualenvwrapper

#usb manager
pacaur -S --noconfirm udisks2 udiskie ntfs-3g dosfstools

#file manager
pacaur -S --noconfirm ranger