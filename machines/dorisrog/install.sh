printf "Executing %s install on mode %s" "$machine" "$env"
cd ~/Projects/dotfiles/scripts/arch
env=$env ./remote/virtualbox_guest.sh
./graphics/nvidia.sh
./graphics/x_server.sh
env=$env ./remote/virtualbox_host.sh
./remote/ssh.sh
./hardware/mouse_input.sh
./hardware/network.sh
./desktop_environment/i3_env.sh
./desktop_environment/filesystem_management.sh
./desktop_environment/color_config.sh
./fonts.sh
./cli_tools.sh
./web/browser.sh
./web/dropbox.sh
./web/skype.sh
./web/torrent.sh
./multimedia/media_essentials.sh
./multimedia/media_optionals.sh
./shell.sh

#generate config files
cd ~/Projects/dotfiles/machines/$machine
env=$env ./firstconfig.sh