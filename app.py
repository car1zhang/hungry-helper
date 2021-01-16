from flask import Flask, url_for, render_template, request
import requests, json

app = Flask(__name__)

f_request = ''
search_url = 'https://api.spoonacular.com/recipes/complexSearch?'
id_url = "https://api.spoonacular.com/recipes/"
api_key = '09e6cdabd57e434ca76916051f205189'

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

# what if use_query is false???
if use_query:
    f_request = search_url + "query=" + params['query']

if use_cuisine:
    f_request += ("&cuisine=" + params['cuisine'])

if use_diet:
    f_request += ("&diet=" + params['diet'])

if use_intolerances:
    f_request += ("&intolerances=" + params['intolerances'])

if use_includeIngredients:
    f_request += ("&includeIngredients=" + params['includeIngredients'])

if use_excludeIngredients:
    f_request += ("&excludeIngredients=" + params['excludeIngredients'])

if use_type:
    f_request += ("&type=" + params['type'])

if use_instructionsRequired:
    f_request += ("&instructionsRequired=" + params['instructionsRequired'])

if use_fillIngredients:
    f_request += ("&fillIngredients=" + params['fillIngredients'])

if use_addRecipeInformation:
    f_request += ("&addRecipeInformation=" + params['addRecipeInformation'])

if use_addRecipeNutrition:
    f_request += ("&addRecipeNutrition=" + params['addRecipeNutrition'])

if use_maxReadyTime:
    f_request += ("&maxReadyTime=" + params['maxReadyTime'])

if use_ignorePantry:
    f_request += ("&ignorePantry=" + params['ignorePantry'])

if use_sort:
    f_request += ("&sort=" + params['sort'])

if use_maxCalories:
    f_request += ("&maxCalories=" + params['maxCalories'])

if use_number:
    f_request += ("&number=" + params['number'])

f_request += ("&apiKey=" + api_key)

@app.route("/")
@app.route("/home")
def main():
    return render_template("home.html", input = "")

@app.route("/", methods=["POST"])
@app.route("/home", methods=["POST"])
def post():
    r_ingredients = request.form["ingredients"]
    r_restrictions = request.form["restrictions"]
    results = requests.get(search_url + "includeIngredients=" + r_ingredients + "&excludeIngredients=" + r_restrictions + "&apiKey=" + api_key).json()
    top_result = results["results"][0]
    top_name = top_result["title"]
    return render_template("home.html", name = top_name, link = top_result)

# TODO: Use react to add more ingredients and make the page more interactive
# TODO: Format results
# TODO: Add more filters
# TODO: Find a way to deploy the site
# TODO: Make footer and about page
# TODO: Make the site look more pleasant
# TODO: Add help feature