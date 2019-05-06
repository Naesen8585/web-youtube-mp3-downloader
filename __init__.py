'''
general idea:
Use flask to present a webpage which takes in the youtube video
and a dropdown menu of the available download formats

Does some snazzy 'processing' thing,
then returns it as the file to download.

'''
from flask import Flask, render_template, request, redirect, Response
from flask import make_response, send_file
from helpers import *
import sys
import re
app = Flask(__name__)
# app.config.from_object("config")

portnumber = sys.argv[1]
chunk_size = int(sys.argv[2])


@app.route('/download/<filename>')
def music_from_youtube(filename):
    print('returning file...')
    chunksize = chunk_size
    return Response(
        return_file(filename, chunksize),
        mimetype='application/octet-stream',
        headers={"Content-Disposition":
                 "attachment;filename=%s" % filename}
    )


@app.route('/')
def index():
    return render_template("index.html", linkdata="")


@app.route('/upload', methods=["POST"])
def getdata():

    youtubelink = request.form['ytlink']
    filetype = request.form['filetype']
    print("Performing download and extraction ops")
    filename = downloadfromyoutube(youtubelink, filetype, app)
    # print(filename)
    # if filename[0] == "‡":
    # print(type(downloadfromyoutube(youtubelink, filetype, app)))
    # mytest = (Response(downloadfromyoutube(
    #    youtubelink, filetype, app), mimetype='text/html'))
    # print(mytest)
    # print(type(mytest))
    #testing = str(mytest)
    # if not testing.startswith("b'[") and testing.endswith(str(filetype), len(testing) - 1):
    #    return render_template("index.html", linkdata=(str(testing)))
    # else:
    return render_template("index.html", linkdata=(filename))
    # else:
    # return render_template("index.html", linkdata=(downloadfromyoutube(youtubelink, filetype, app)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=portnumber, debug=True)
