#Update and optimize mirrorlist for pacman
#Code taken from a linode stackscript and added sudo -v to it
#https://www.linode.com/stackscripts/view/12580
sudo -v pacman -Sy --noconfirm --needed wget reflector
sudo -v mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.old
sudo -v wget https://www.archlinux.org/mirrorlist/all/ -O /etc/pacman.d/mirrorlist
sudo -v reflector --verbose --protocol http --sort rate --fastest 6 --threads 10 --save /etc/pacman.d/mirrorlist
sudo -v pacman -Syu --noconfirm

#Get archsetup and dotfiles project
sudo -v pacman -S --noconfirm --needed git openssh stow
mkdir ~/Projects
git clone gitsandman:anhtuann/archsetup.git ~/Projects/archsetup
git clone gitsandman:anhtuann/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
git checkout tardis
stow -v -t ~ git
sudo -v rm /etc/pacman.conf
sudo -v stow -v -t / pacman
cd ~/Projects/archsetup
git checkout 20171121_tardis_vbinstall
sudo -v pacman -Syu --noconfirm
