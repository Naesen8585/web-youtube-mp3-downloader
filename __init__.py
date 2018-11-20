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
    filename = downloadfromyoutube(youtubelink, filetype)
    return render_template("index.html", linkdata=(filename))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=portnumber, debug=True)
