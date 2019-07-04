# web-youtube-mp3-downloader

This project aims to provide a web interface which will allow extraction of audio files from youtube videos.

To install this, all you need to do is run

`curl -L https://raw.githubusercontent.com/Naesen8585/web-youtube-mp3-downloader/master/auto-installer.bash | bash`


However, if you'd like to download from Github manually either via zip or git, all you need to do is run

`bash install_webytdl.bash`

In the directory that you download from Git.

You will be prompted which port number you want it to run on, and then when installation is completed, you will be prompted to reboot.

Once rebooted, you will be able to access your server at `your IP Address:Your Port Number`

To use it, All you need to do is paste the address of the Youtube, Bitchute, Dailymotion, or other hosting provider's video you want to extract the link from. Select the type of audio file you'd like to be ripped from the video, and then submit the data. You'll see the pretty `Processing` animation until the data is extracted and converted, and then you will be prompted to download it from your browser. This works with mobile browsers too!

Note that if you start getting `None` returned for your file to extract, it's likely your video provider has updated their methods of preventing you from obtaining the videos. The good news is that the `youtube-dl` team keeps pretty well on top of this as well. To debug, simply reboot or power off and on your machine, and the system will update youtube-dl automatically.

If that's not compatible, you can manually update `youtube-dl` using pip. Both pip and pip3 versions need to be updated. If you don't know how to do this, just reboot your system and you'll be good to go.
