#! /bin/sh
basedirectory=$1
portnumber=$2
chunksize=$3

while [ ! -d "$basedirectory" ]
do
        echo "loading directory"
done


if [ -d "$basedirectory" ]; then
  sudo pip3 install -U youtube-dl
  sudo pip install -U youtube-dl
  python3 $basedirectory/__init__.py $portnumber $chunksize
fi
