#Update and optimize mirrorlist for pacman
#Code taken from a linode stackscript and added sudo to it
#https://www.linode.com/stackscripts/view/12580
sudo pacman -Sy --noconfirm wget reflector
sudo mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.old
sudo wget https://www.archlinux.org/mirrorlist/all/ -O /etc/pacman.d/mirrorlist
sudo reflector --verbose --protocol http --sort rate --fastest 6 --threads 10 --save /etc/pacman.d/mirrorlist
sudo pacman -Syu --noconfirm

#Get archsetup and dotfiles project
sudo pacman -S --noconfirm git openssh stow
mkdir ~/Projects
git clone gitsandman:anhtuann/archsetup.git ~/Projects/archsetup
git clone gitsandman:anhtuann/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
git checkout tardis
stow -v -t ~ git
sudo rm /etc/pacman.conf
sudo stow -v -t / pacman
cd ~/Projects/archsetup
git checkout 20171121_tardis_vbinstall
sudo pacman -Syu --noconfirm
