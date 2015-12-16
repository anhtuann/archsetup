#option configuration
PS3='Which environment is it :'
options=("test" "real")
select opt in "${options[@]}"
do
    case $opt in
        "test")
            environment="test"
            break
            ;;
        "real")
            environment="real"
            break
            ;;
        *) echo invalid option;;
    esac
done

#sort mirrors by speed
if [ $environment == "real" ]
    then
        echo 'Sorting mirrors by speed'
        sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
        sudo sh -c 'rankmirrors -n 5 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirrorlist'
        sudo pacman -Syu
fi

#ssh keys
sudo pacman -S --noconfirm openssh
if [ $environment == "test" ]
    then
        ssh-keygen
fi
echo 'eval $(ssh-agent)' >> ~/.xinitrc

#graphic drivers
if [ $environment == "test" ]
    then
        echo 'Installing virtualbox graphic driver'
        sudo pacman -S --noconfirm virtualbox-guest-utils
else
    echo 'Installing nvidia driver'
    sudo pacman -S --noconfirm nvidia
fi

#Xserver
sudo pacman -S --noconfirm xorg-server xorg-server-utils xorg-apps
sudo pacman -S --noconfirm xorg-xinit
sudo pacman -S --noconfirm lxrandr

#i3 initialisation
sudo pacman -S --noconfirm i3

#git for pacaur install
sudo pacman -S --noconfirm git
git config --global push.default simple

#pacaur install
sudo pacman -S --noconfirm expac
mkdir /tmp/aur
cd /tmp/aur
git clone http://aur.archlinux.org/cower.git
git clone http://aur.archlinux.org/pacaur.git
gpg --recv-keys 1EB2638FF56C0C53
cd cower
makepkg -s
sudo pacman -U --noconfirm cower*.pkg.tar.xz
cd ../pacaur
makepkg -s
sudo pacman -U --noconfirm pacaur*.pkg.tar.xz
cd
mkdir -p ~/.config/pacaur
echo "displaybuildfiles=none" > ~/.config/pacaur/config

#various applications for i3+firefox
pacaur -S --noconfirm rxvt-unicode
pacaur -S --noconfirm xf86-input-libinput 
pacaur -S --noconfirm ttf-hack
pacaur -S --noconfirm firefox
pacaur -S --noconfirm light-git
pacaur -S --noconfirm rofi scrot feh volumeicon dunst

#dotfiles downloaded from github
mkdir ~/Projects 
cd ~/Projects
git clone https://github.com/anhtuann/dotfiles.git

#useful scripts downloaded from github
git clone https://github.com/anhtuann/useful-scripts.git

#vim
pacaur -S --noconfirm vim

#various utilities
pacaur -S --noconfirm alsa-utils
pacaur -S --noconfirm xclip
pacaur -S --noconfirm transmission-cli
pacaur -S --noconfirm imagemagick
pacaur -S --noconfirm ttf-mplus
pacaur -S --noconfirm unrar
pacaur -S --noconfirm rsync

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

#useful softwares
pacaur -S --noconfirm calibre blender

#virtualbox
pacaur -S --noconfirm virtualbox linux-headers
sudo dkms install vboxhost/$(pacman -Q virtualbox|awk '{print $2}'|sed 's/\-.\+//') -k $(uname -rm|sed 's/\ /\//')
sudo gpasswd -a $USER vboxusers
pacaur -S --noconfirm virtualbox-guest-iso net-tools
pacaur -S --noconfirm virtualbox-ext-oracle qt4


#generate config files
/bin/bash ~/Projects/useful-scripts/arch_install/genconf.sh
