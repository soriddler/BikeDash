from flask import Flask, render_template, redirect, request
from watcher import Watcher
import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)
app = Flask(__name__)
distance = 0.1

@app.route("/")
def home():
    #return render_template('overview/index.html', status=True)
    return render_template('subfolder/page.html', distance=distance)

@app.route("/setdistance", methods=["POST"])
def setdistance():
    global distance
    distance = float(request.form["distance"])
    logging.info(f"set distance to {distance}")
    return redirect(request.referrer)  

if __name__ == '__main__':
    app.run(debug = True)
    # logging.info("Starting up application ...")
    # w = Watcher()
    # w.DIRECTORY_TO_WATCH = "/usr/src/app/database"
    # w.run()