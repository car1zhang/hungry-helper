from flask import Flask, url_for, render_template, request
import requests, json

app = Flask(__name__)

frequest = ''
url = 'https://api.spoonacular.com/recipes/complexSearch?'
api_key = '58dec5f444fb4942b7a123310f0eb653'

use_query = True
use_cuisine = False
use_diet = False
use_intolerances = False
use_includeIngredients = False
use_excludeIngredients = False
use_type = False  # Main course, dessert etc.
use_instructionsRequired = True
use_fillIngredients = True
use_addRecipeInformation = False
use_addRecipeNutrition = False
use_maxReadyTime = False
use_ignorePantry = True
use_sort = True
use_maxCalories = False
use_number = True

params = {
    'query': 'lasagna',
    'cuisine': '',
    'diet': '',
    'intolerances': '',
    'includeIngredients': '',
    'excludeIngredients': '',
    'type': '',
    'instructionsRequired': 'True',
    'fillIngredients': 'True',
    'addRecipeInformation': '',
    'addRecipeNutrition': '',
    'maxReadyTime': '',
    'ignorePantry': 'True',
    'sort': 'calories',
    'maxCalories': '',
    'number': '1'
}

if use_query:
    frequest = url + "query=" + params['query']

if use_cuisine:
    frequest += ("&cuisine=" + params['cuisine'])

if use_diet:
    frequest += ("&diet=" + params['diet'])

if use_intolerances:
    frequest += ("&intolerances=" + params['intolerances'])

if use_includeIngredients:
    frequest += ("&includeIngredients=" + params['includeIngredients'])

if use_excludeIngredients:
    frequest += ("&excludeIngredients=" + params['excludeIngredients'])

if use_type:
    frequest += ("&type=" + params['type'])

if use_instructionsRequired:
    frequest += ("&instructionsRequired=" + params['instructionsRequired'])

if use_fillIngredients:
    frequest += ("&fillIngredients=" + params['fillIngredients'])

if use_addRecipeInformation:
    frequest += ("&addRecipeInformation=" + params['addRecipeInformation'])

if use_addRecipeNutrition:
    frequest += ("&addRecipeNutrition=" + params['addRecipeNutrition'])

if use_maxReadyTime:
    frequest += ("&maxReadyTime=" + params['maxReadyTime'])

if use_ignorePantry:
    frequest += ("&ignorePantry=" + params['ignorePantry'])

if use_sort:
    frequest += ("&sort=" + params['sort'])

if use_maxCalories:
    frequest += ("&maxCalories=" + params['maxCalories'])

if use_number:
    frequest += ("&number=" + params['number'])

frequest += ("&apiKey=" + api_key)

@app.route("/")
@app.route("/home")
def main():
    return render_template("home.html", input = "")

@app.route("/", methods=["POST"])
@app.route("/home", methods=["POST"])
def post():
    return render_template("home.html", ingredients = request.form["ingredients"], restrictions = request.form["restrictions"])