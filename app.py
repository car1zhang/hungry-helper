import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Api info
search_url = 'https://api.spoonacular.com/recipes/complexSearch?'
id_url = 'https://api.spoonacular.com/recipes/'
empty_image_url = 'https://t4.ftcdn.net/jpg/01/92/21/99/360_F_192219965_or6uDv1LE5PvjjbTFxjpt6xM5OzoWvWA.jpg'
api_key = '58dec5f444fb4942b7a123310f0eb653'  # alternate key: 58dec5f444fb4942b7a123310f0eb653

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
    'maxReadyTime': '',  # TODO
    'ignorePantry': 'True',
    'sort': 'max-used-ingredients',  # or min-missing-ingredients
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

    # results = requests.get(search_url + paramstring + '&apiKey=' + api_key).json()
    # print(results)

    return results


# get_recipe(params)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


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

    if len(ingredientList) == 0 and len(intoleranceList) == 0 and r_diet == "" and r_query == "":
        return render_template('result.html', code=1)

    # Getting recipes from api
    results = get_recipe(params)

    try:
        result = results['results'][0]

        calories = str(results['results'][0]['nutrition']['nutrients'][0]['amount']) + \
                   ' ' + results['results'][0]['nutrition']['nutrients'][0]['unit']

        title = result['title']
        image_url = result['image']
        url = result['sourceUrl']

    except(IndexError):
        return render_template('result.html', code=2)
    except(KeyError):
        return render_template('result.html', code=2)

    return render_template('result.html', code=0, image=image_url, name=title, url=url)

# Carl TODO
# TODO: Clear button
# TODO: Delete button
# TODO: Write Devpost stuff
# TODO Optional: Make footer and about page
# TODO Optional: Add help feature
