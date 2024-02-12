import os # A portable way of interacting
from flask import Flask, render_template # The render_template function is used to render HTML templates


app = Flask(__name__)

@app.route("/")
def imdex():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
    host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=True)