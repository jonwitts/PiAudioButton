#!/bin/bash

# Setup script to install our required software and 
# configure start up etc.

# Make sure script is run as root.
if [ "$(id -u)" != "0" ]; then
  echo "Must be run as root with sudo! Try: sudo ./setup.sh"
  exit 1
fi

# update and upgrade existing packages
echo "Upgrading existing packages"
echo "=========================="
apt-get update
apt-get dist-upgrade -y

# install our required packages
echo "Installing dependencies..."
echo "=========================="
apt-get install git python3 -y
apt-get install python3-gpiozero python3-pygame -y

# clone our repo from GitHub
cd /
git clone https://github.com/jonwitts/PiAudioButton.git

# Add python script to rc.local
echo "Add Python script to rc.local"
echo "=========================="
sed -i -e '$i sudo /PiAudioButton/PiAudioButtonMain.py &\n' /etc/rc.local

# set our Pi to output audio through the 3.5mm jack
# and turn the volume up
amixer cset numid=3 1
amixer set 'PCM' 90%

# done
echo "Done. Rebooting now"
echo "=========================="
reboot
