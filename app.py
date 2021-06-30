from flask import Flask, render_template, redirect, request
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)
app = Flask(__name__)
distance = 0.1

@app.route("/")
def home():
    #return render_template('overview/index.html', status=False, temperature=25.02)
    return render_template('subfolder/page.html', distance=distance)

@app.route("/setdistance", methods=["POST"])
def setdistance():
    global distance
    distance = float(request.form["distance"])
    logging.info(f"set distance to {distance}")
    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(debug = True)