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
    'addRecipeInformation': 'True',  # TODO
    'addRecipeNutrition': 'True',  # TODO
    'maxReadyTime': 'True',  # TODO
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
    r_includeIngredients = list(set(request.form.getlist('ingredients[]')))
    r_intolerances = list(set(request.form.getlist("restrictions[]")))
    r_diet = request.form.get('diet')
    r_query = request.form.get('query')

    ingredientList = r_includeIngredients[0]

    for n in range(1, len(r_includeIngredients)):
        ingredientList += (',' + r_includeIngredients[n])

    intoleranceList = r_intolerances[0]

    for n in range(1, len(r_intolerances)):
        intoleranceList = (',' + r_intolerances[0])

    # Setting request params
    params['includeIngredients'] = ingredientList
    params['intolerances'] = intoleranceList
    params['diet'] = r_diet
    params['query'] = r_query

    if len(ingredientList) == 0 and len(intoleranceList) == 0 and r_diet == 0 and r_query == 0:
        return render_template('home.html', name='Please enter some search criteria')

    # Getting recipes from api
    results = get_recipe(params)

    top_result = ''
    calories = ''
    image_url = ''

    try:
        top_result = results['results'][0]['title']

        calories = str(results['results'][0]['nutrition']['nutrients'][0]['amount']) + \
                   ' ' + results['results'][0]['nutrition']['nutrients'][0]['unit']

        image_url = results['results'][0]['image']

    except(IndexError):
        top_result = 'Sorry, we do not have a recipe matching your search criteria. \n Please check your spelling and make sure all information was entered correctly'

    return render_template('home.html', image=image_url, name=top_result, calories=calories)

# Carl TODO
# TODO: Format results
# TODO: Add more filters
# TODO: Make footer and about page
# TODO: Make the site look more pleasant
# TODO Optional: Add interactive elements to the page
# TODO Optional: Add help feature

# Hosted by ngrok  at http://c08dbd1b8351.ngrok.io/
