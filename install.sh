#!/bin/bash
vermelho="\e[31m"
verde="\e[32m"
amarelo="\e[33m"
azul="\e[34m"
roxo="\e[38;2;128;0;128m"
reset="\e[0m"

rm -rf /root/StartNet/
rm -f /usr/local/bin/StartNet
pkill -9 -f "/root/StartNet/checkuser.py"

apt update && apt upgrade -y && apt install python3 git -y
git clone https://github.com/Stalkermtx/StartNetCheckUser.git
chmod +x /root/StartNet/checkuserMenu.sh
ln -s /root/StartNet/checkuserMenu.sh /usr/local/bin/StartNetCheckuser

clear
echo -e "Para Iniciar o Menu Digite: ${verde}StartNet${reset}"
