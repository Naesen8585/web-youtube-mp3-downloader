#!/usr/bin/python3

import subprocess
import sys
import re
import string
import os
import shutil

# download the file, load it in to memory, delete it from disk, return it.


def downloadfromyoutube(vid_url, audio_format):
    cmd = ["youtube-dl", vid_url, "--no-warnings", "--restrict-filenames",
           "--extract-audio", "--audio-format", str(audio_format)]
    returnlist = []
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in proc.stdout.readlines():
        print("doing list appending stuff")
        returnlist.append(str(line))
    finalmp3filename = ""
    for item in returnlist:
        printstring = ("Finding the %s filename...", (audio_format))
        print(printstring)
        if (re.search("ffmpeg", item) and re.search("Destination", item)):
            arraytosplit = item.split(" ")
            finalmp3filename = arraytosplit[-1]
            print("found it!")
            break
    print(finalmp3filename)
    finalmp3filearray = finalmp3filename.split('\\n')
    finalmp3filename = finalmp3filearray[0]
    return finalmp3filename


def return_file(filename, chunk_size):
    print("File size: %s" % os.path.getsize(filename))
    content_file = open(filename, 'rb')
    while True:
        content = content_file.read(chunk_size)
        if not content:
            print("File has been completely passed.")
            os.remove(filename)
            if os.path.isdir("./__pycache__"):
                shutil.rmtree("./__pycache__")
            break

        yield content
    content_file.close()
