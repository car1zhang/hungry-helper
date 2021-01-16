import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Api info
search_url = 'https://api.spoonacular.com/recipes/complexSearch?'
id_url = "https://api.spoonacular.com/recipes/"
api_key = '57124f77baee4ec4b7941512d5819c8c'  # other key: 09e6cdabd57e434ca76916051f205189 , 58dec5f444fb4942b7a123310f0eb653

# Params for query
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


@app.route("/")
@app.route("/home")
def main():
    return render_template("home.html", input="")


@app.route("/", methods=["POST"])
@app.route("/home", methods=["POST"])
def post():
    paramstring = ''

    r_includeIngredients = request.form["ingredients"]
    r_intolerances = request.form["restrictions"]

    # Updating request params
    params['includeIngredients'] = r_includeIngredients
    params['intolerances'] = r_intolerances

    # Removing null params
    for key, value in params.items():
        if value != '':
            paramstring += ("&" + key + "=" + value)

    results = requests.get(search_url + paramstring + "&apiKey=" + api_key).json()

    top_result = results["results"][0]
    top_name = top_result["title"]

    return render_template("home.html", name=top_name, link=top_result)

    r_ingredients = request.form["ingredients"]
    r_restrictions = request.form["restrictions"]

    results = requests.get(search_url + "includeIngredients=" + r_ingredients + "&excludeIngredients=" + r_restrictions + "&apiKey=" + api_key).json()["results"]
    top_result = (results[0] if len(results) else None)
    top_name = (top_result["title"] if top_result else None)
    return render_template("home.html", name = r_ingredients, link = top_result)

# TODO: Use react to add more ingredients and make the page more interactive
# TODO: Format results
# TODO: Add more filters
# TODO: Find a way to deploy the site
# TODO: Make footer and about page
# TODO: Make the site look more pleasant
# TODO: Add help feature
