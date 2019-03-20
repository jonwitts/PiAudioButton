#!/bin/bash

# Setup script to install our required software and 
# configure services etc.

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

# clone our repo from GitHub and move into directory
cd /
git clone https://github.com/jonwitts/PiAudioButton.git
cd /piAudioButton

# copy and activate our systemd definitions
echo "Copy and activate our systemd definitions..."
echo "=========================="
# PiAudioButton service
cp ./PiAudioButton.service /lib/systemd/system/PiAudioButton.service
chmod 644 /lib/systemd/system/PiAudioButton.service

# shutdownAudio service
cp ./shutdownAudio.service /lib/systemd/system/shutdownAudio.service
chmod 644 /lib/systemd/system/shutdownAudio.service

# reload and enable
systemctl daemon-reload
systemctl enable PiAudioButton.service
systemctl enable shutdownAudio.service

# done
echo "Done. Rebooting now"
echo "=========================="
reboot
