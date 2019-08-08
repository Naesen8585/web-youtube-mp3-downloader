#!/usr/bin/python3
from __future__ import unicode_literals
import subprocess
import sys
import re
import string
import os
import shutil
from flask import Flask, render_template, request, redirect, Response
from flask import make_response, send_file
import time
import youtube_dl


'''
8/7/2019 : Update to use youtube-dl's inherent pythonic capabilities instead of using pure subprocess, will work on
how to handle the bitchute code next
'''


# download the file, load it in to memory, delete it from disk, return it.

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


finalfilename = ""


def downloadfromyoutube(vid_url, audio_format):
    global finalfilename

    class MyLogger(object):

        def debug(self, msg):
            global finalfilename

            print("Debug")
            print(msg)
            if (re.search("file:", str(msg)) and re.search(str(audio_format), msg)):
                # we extract the name of the file here and then return it
                finalfilename = msg.split('file:')[-1]
            if (re.search("Deleting original file", msg)):
                print("Returning the final file name of")
                print(finalfilename)

        def warning(self, msg):
            print("Warning")
            print(msg)

        def error(self, msg):
            print("Error")
            print(msg)

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
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': str(audio_format),
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'verbose': 1,
        'restrictfilenames': 1,
        'nocheckcertificate': 1,  # for bitchute compatibility
        'no_color': 1,
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(vid_url)])
    if (len(finalfilename) > 0):
        return(finalfilename)
    else:
        return("There was an error processing your video, no file available.")


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
