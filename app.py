import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Api info
search_url = 'https://api.spoonacular.com/recipes/complexSearch?'
id_url = "https://api.spoonacular.com/recipes/"

api_key = '7daff3f13857445097e41523fc01d44a'  # other key: 58dec5f444fb4942b7a123310f0eb653

# Params for query
params = {
    'query': '',
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


def get_recipe(params):
    paramstring = ''

    # Removing null params
    for key, value in params.items():
        if value != '':
            paramstring += ("&" + key + "=" + value)

    results = requests.get(search_url + paramstring + "&apiKey=" + api_key).json()

    return results


@app.route("/")
@app.route("/home")
def main():
    return render_template("home.html", input="")


@app.route("/", methods=["POST"])
@app.route("/home", methods=["POST"])
def post():
    r_includeIngredients = request.form["ingredients"]
    r_intolerances = request.form["restrictions"]

    # Updating request params
    params['includeIngredients'] = r_includeIngredients
    params['intolerances'] = r_intolerances

    results = get_recipe(params, search=True)

    try:
        top_result = results["results"][0]["title"]

    except(IndexError):
        top_result = ['No such recipe exists']

    return render_template("home.html", name=top_result)

# TODO: Use react to add more ingredients and make the page more interactive
# TODO: Format results
# TODO: Add more filters
# TODO: Find a way to deploy the site
# TODO: Make footer and about page
# TODO: Make the site look more pleasant
# TODO: Add help feature
