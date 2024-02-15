import os # A portable way of interacting
import json
from flask import Flask, render_template # The render_template function is used to render HTML templates


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # Open the json file as "r" read-only and assign the content json_data
    with open("data/company.json", "r") as json_data: # Open the JSON file in order to read it.
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data) # Expression to display about.html on page from backend to frontend

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)

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