from flask import Flask, url_for, render_template
import requests, json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("home.html", data = requests.get("https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=58dec5f444fb4942b7a123310f0eb653").json())