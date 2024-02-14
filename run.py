import os # A portable way of interacting
from flask import Flask, render_template # The render_template function is used to render HTML templates


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1,2,3]) # Expression to display about.html on page from backend to frontend


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact") # Expression to display contact.html on page from backend to frontend


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers") # Expression to display careers.html on page from backend to frontend

if __name__ == "__main__":
    app.run(
    host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=True)