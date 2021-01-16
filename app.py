from flask import Flask, url_for, render_template
import requests, json

app = Flask(__name__)

request = ''
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
    request = url + "query=" + params['query']

if use_cuisine:
    request += ("&cuisine=" + params['cuisine'])

if use_diet:
    request += ("&diet=" + params['diet'])

if use_intolerances:
    request += ("&intolerances=" + params['intolerances'])

if use_includeIngredients:
    request += ("&includeIngredients=" + params['includeIngredients'])

if use_excludeIngredients:
    request += ("&excludeIngredients=" + params['excludeIngredients'])

if use_type:
    request += ("&type=" + params['type'])

if use_instructionsRequired:
    request += ("&instructionsRequired=" + params['instructionsRequired'])

if use_fillIngredients:
    request += ("&fillIngredients=" + params['fillIngredients'])

if use_addRecipeInformation:
    request += ("&addRecipeInformation=" + params['addRecipeInformation'])

if use_addRecipeNutrition:
    request += ("&addRecipeNutrition=" + params['addRecipeNutrition'])

if use_maxReadyTime:
    request += ("&maxReadyTime=" + params['maxReadyTime'])

if use_ignorePantry:
    request += ("&ignorePantry=" + params['ignorePantry'])

if use_sort:
    request += ("&sort=" + params['sort'])

if use_maxCalories:
    request += ("&maxCalories=" + params['maxCalories'])

if use_number:
    request += ("&number=" + params['number'])

request += ("&apiKey=" + api_key)

@app.route("/")
@app.route("/home")
def main():
    return render_template("home.html", data = requests.get(request).json())