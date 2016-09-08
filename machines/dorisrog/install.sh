printf "Executing %s install on mode %s" "$machine" "$env"

cd ~/Projects/dotfiles/scripts/arch
env=$env ./laptop/graphic_drivers.sh
env=$env ./laptop/virtualbox.sh
env=$env ./laptop/hardware.sh
./laptop/window_manager.sh
./fonts.sh
./laptop/web.sh
./python.sh
./laptop/various_softwares.sh
./syncplay.sh
./shell.sh

if [ $env == "real" ]; then
    cd ~/Projects/dotfiles/scripts/arch/laptop
    ./android.sh
    ./bluetooth.sh
    ./playonlinux.sh
fi

#generate config files
cd ~/Projects/dotfiles/machines/dreamland
env=$env ./firstconfig.sh
mkdir /home/anhtuann/.config/dunst
ln -sf /home/anhtuann/Projects/dotfiles/machines/dreamland/confs/dunst_conf /home/anhtuann/.config/dunst/dunstrc
pacaur -S zsh
