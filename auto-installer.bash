#!/bin/bash

echo "This will install the required libraries for the web-youtube-mp3-downloader"
echo "and set it up as a system service to start when your system boots."


echo "Now installing the required python3 libraries as well as youtube-dl"
sudo apt-get update && sudo apt-get install python3 python3-pip python3-dev python python-pip python-dev -y
sudo pip3 install flask -U
sudo pip install -U youtube-dl
sudo pip3 install -U youtube-dl
sudo apt-get install unzip -y
echo "Now updating the crontab for the current user..."

read -p "Which port would you like this to run on? " portnumber

wget https://github.com/Naesen8585/web-youtube-mp3-downloader/archive/master.zip && unzip master.zip && rm master.zip

cd web-youtube-mp3-downloader-master
currentdir=$(pwd)
touch ./oldcron
crontab -l | cat >./oldcron



shellpath=$(which bash)

read -e -p "Please enter the maximum chunk size in bytes (default is 1 MB, If you don't know what this means leave it default): " -i "1024000" chunksize

echo "copying the starterscript to your home directory..."

cp $currentdir/starterscript.sh ~

echo "@reboot $shellpath ~/starterscript.sh $currentdir $portnumber $chunksize" >> ./oldcron

crontab ./oldcron

echo "Crontab updated. Now on reboot, the server will start on port $portnumber."
echo "If you ever need to move this program, make sure you update your crontab"
echo "to remove the entry done by this file, then when you move "
echo "the entire directory this is in to somewhere else, run this script."
echo "This program will only work if everything is kept bundled in the same folder."
echo "We recommend you reboot your system to complete the installation process."
read -p "Press enter to reboot your system. Press CTRL+C to not." </dev/tty

sudo reboot
