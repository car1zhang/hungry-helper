import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Api info
search_url = 'https://api.spoonacular.com/recipes/complexSearch?'
id_url = 'https://api.spoonacular.com/recipes/'

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
            paramstring += ('&' + key + '=' + value)

    results = requests.get(search_url + paramstring + '&apiKey=' + api_key).json()

    return results


@app.route('/')
@app.route('/home')
def main():
    return render_template('home.html', input='')


@app.route("/", methods=['POST'])
@app.route("/home", methods=['POST'])
def post():
    paramstring = ''

    # This is what is actually important (what changed)
    r_includeIngredients = request.form.getlist('ingredients[]')
    r_intolerances = request.form.getlist("restrictions[]")
# >>>>>>> Stashed changes

    # Updating request params
    params['includeIngredients'] = r_includeIngredients
    params['intolerances'] = r_intolerances

# <<<<<<< Updated upstream
    results = get_recipe(params)

    try:
        top_result = results['results'][0]['title']
        calories = str(results['results'][0]['nutrition']['nutrients'][0]['amount']) + \
                   ' ' + results['results'][0]['nutrition']['nutrients'][0]['unit']
        image_url = results['results'][0]['image']

    except(IndexError):
        top_result = 'Sorry, we do not have a recipe matching your search criteria.'

    return render_template('home.html', image = image_url, name=top_result, calories=calories)

# TODO: Use react to add more ingredients and make the page more interactive
# =======
    # Removing null params
    for value in r_includeIngredients:
        if value != '':
            paramstring += ("&" + "includeIngredients" + "=" + value)

    results = requests.get(search_url + paramstring + "&apiKey=" + api_key).json()
    top_result = results["results"][0]
    return render_template("home.html", name = top_result)

# Carl TODO
# TODO: Format results
# TODO: Add more filters
# TODO: Make footer and about page
# TODO: Make the site look more pleasant
# TODO Optional: Add interactive elements to the page
# TODO Optional: Add help feature

# Aayush TODO
# TODO: Fix search functionality
# TODO: Find a way to deploy the site
