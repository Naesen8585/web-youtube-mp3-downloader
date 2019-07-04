#!/usr/bin/python3
import subprocess
import sys
import re
import string
import os
import shutil
from flask import Flask, render_template, request, redirect, Response
from flask import make_response, send_file
import time

# download the file, load it in to memory, delete it from disk, return it.


def downloadfromyoutube(vid_url, audio_format, flaskapp):

    if re.search("bitchute", str(vid_url).lower()):
        try:
            print("this appears to be bitchute. Performing vid url extraction")
            cmdbitchute = ["curl", "-s", str(vid_url), "|", "grep", "-Eoi", "'<source [^>]+>'", "|",
                           "grep", "-Eo", "'src=\"[ ^\\\"]+\"'", "|", "grep", "-Eo", "'(http|https)://[^\"] +'"]

            procbitchute = subprocess.Popen(cmdbitchute, stdout=subprocess.PIPE)
            for stdout_linebitchute in iter(procbitchute.stdout.readline, b''):

                itembitchute = str(stdout_linebitchute)
                vid_url = item123
        except:
            return "Unable to extract bitchute video, no file downloaded."
    print("the vid url passed is ")
    print(vid_url)
    cmd = ["/usr/local/bin/youtube-dl", str(vid_url), "--no-warnings", "--restrict-filenames",
           "--extract-audio", "--audio-format", str(audio_format), "--no-check-certificate"]
    returnlist = []
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    finalvideoname = ""
    videodeleted = False
    finalmp3filename = ""
    for stdout_line in iter(proc.stdout.readline, b''):
        item = str(stdout_line)
        print(item)

        if (re.search("[download]", item) and re.search("Destination", item)):
            arraytosplit = item.split(" ")
            finalvideoname = arraytosplit[-1]
            finalvideoarray = finalvideoname.split('\\n')
            finalvideoname = finalvideoarray[0]
            print("video name is")
            print(finalvideoname)
        if (re.search("ffmpeg", item) and re.search("Destination", item)):
            arraytosplit = item.split(" ")
            finalmp3filename = arraytosplit[-1]

            finalmp3filearray = finalmp3filename.split('\\n')

            finalmp3filename = finalmp3filearray[0]
            print("Mp3 name is")
            print(finalmp3filename)
        if (re.search('Deleting', item)):
            print("Done!")
            print(finalmp3filename)
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
