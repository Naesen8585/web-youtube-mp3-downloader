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

    cmd = ["/usr/local/bin/youtube-dl", str(vid_url), "--no-warnings", "--restrict-filenames",
           "--extract-audio", "--audio-format", str(audio_format), "--youtube-skip-dash-manifest", "--no-color", "--newline"]
    returnlist = []
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    #cmd2 = ["sudo", "renice", "+10", "$(pidof ffmpeg)"]
    # if proc:
    #    proc2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE)
    finalvideoname = ""
    videodeleted = False
    finalmp3filename = ""
    for stdout_line in iter(proc.stdout.readline, b''):
        # yield "‡" + str(stdout_line)
        #stdout_line.rstrip() + '<br/>\n'
        item = str(stdout_line)
        print(item)

        if (re.search("[download]", item) and re.search("Destination", item)):
            arraytosplit = item.split(" ")
            finalvideoname = arraytosplit[-1]
            #print("found it!")
            finalvideoarray = finalvideoname.split('\\n')
            finalvideoname = finalvideoarray[0]
            print("video name is")
            print(finalvideoname)
        if (re.search("ffmpeg", item) and re.search("Destination", item)):
            arraytosplit = item.split(" ")
            finalmp3filename = arraytosplit[-1]
            #print("found it!")
            finalmp3filearray = finalmp3filename.split('\\n')

            finalmp3filename = finalmp3filearray[0]
            print("Mp3 name is")
            print(finalmp3filename)
        if (re.search('Deleting', item)):
            print("Done!")
            print(finalmp3filename)
            return finalmp3filename
            # print(finalmp3filename)
        # if len(finalvideoname) > 0 and len(finalmp3filename) > 0:
        #    if os.path.isfile('./' + finalvideoname):
        #        print("Waiting on the file to be finished...")
        #        # yield "Waiting on file to be finished..."
        #    else:
        #        # yield finalmp3filename
        #        return finalmp3filename

            # yield "‡" + str(stdout_line).rstrip() + '<br/>\n'
        # return Response(str(stdout_line), mimetype='text/html')
    # for line in proc.stdout.readlines():
    #    print("doing list appending stuff")
    #    returnlist.append(str(line))
    #finalmp3filename = ""
    # for item in returnlist:
    #    printstring = ("Finding the %s filename...", (audio_format))
    #    print(printstring)
    #    if (re.search("ffmpeg", item) and re.search("Destination", item)):
    #        arraytosplit = item.split(" ")
    #        finalmp3filename = arraytosplit[-1]
    #        print("found it!")
    #        break
    # print(finalmp3filename)
    #finalmp3filearray = finalmp3filename.split('\\n')
    #finalmp3filename = finalmp3filearray[0]
    # return finalmp3filename


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
