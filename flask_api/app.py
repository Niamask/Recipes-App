from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response


@app.route("/")
def hello_world():
    return "Hello, World!"


recipe = {
        "publisher":"A Spicy Perspective",
        "ingredients":[

            {
            "quantity":None,
            "unit":"",
            "description":"for the pizza dough:"
            },
            {
            "quantity":1,
            "unit":"",
            "description":"1/2 tsp. dry active yeast"
            },
             {
            "quantity":0.75,
            "unit":"cup",
            "description":"warm water"
            },
             {
            "quantity":2,
            "unit":"",
            "description":"tsp.sugar"
            },
             {
            "quantity":0.5,
            "unit":"cup",
            "description":"bread flour"
            },
             {
            "quantity":2,
            "unit":"",
            "description":"td. olive oil + extra for bowl"
            },
             {
            "quantity":1,
            "unit":"",
            "description":"1/2 tsp. sea salt"
            },
             {
            "quantity":None,
            "unit":"",
            "description":"For the greek pizza"
            },
             {
            "quantity":1,
            "unit":"",
            "description":"lb. pizza dough recipe above"
            },
             {
            "quantity":1,
            "unit":"",
            "description":"lb. hummus any variety"
            },
             {
            "quantity":1,
            "unit":"cup",
            "description":"baby arugula"
            },
             {
            "quantity":0.67,
            "unit":"cup",
            "description":"good pitted greek olives"
            },
             {
            "quantity":0.67,
            "unit":"cup",
            "description":"cherry or grape tomatoes halved"
            },
             {
            "quantity":0.25,
            "unit":"cup",
            "description":"crumbled fet cheese"
            }, 
            {
            "quantity":None,
            "unit":"cup",
            "description":"Drizzle of good olive oil"
            }

        ],
        "source_url":"http://www.aspicyperspective.com/2012/07/greek-pizza-grilled.html",
	    "image_url":"http://forkify-api.herokuapp.com/images/IMG_4351180x1804f4a.jpg",
	    "title":"Greek Pizza",
        "servings":4,
        "cooking_time":75,
	    "id":"5ed6604591c37cdc054bca3b"
}


@app.route("/recipe")
def get_recipe():
    return jsonify(recipe)


@app.route("/recipe/<string:recipe_code>")
def get_recipe_by_id(recipe_code):
    recipe = next((recipe for recipe in recipe if recipe["id"] == recipe_code), None)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({"error": "Recipe not found"}), 404

fall_recipe = {
    "status":'success',
    "data": {"recipe": recipe}
}

@app.route("/fall_recipe")
def get_y():
    return jsonify(fall_recipe)

recipes = {

	0:{
        "publisher":"Closet Cooking",
	    "image_url":"http://forkify-api.herokuapp.com/images/BBQChickenPizzawithCauliflowerCrust5004699695624ce.jpg",
	    "title":"Cauliflower Pizza Crust (with BBQ Chicken Pizza)",
	    "id":"5ed6604591c37cdc054bcd09",

	},
    1:{
        "publisher":"Closet Cooking",
        "image_url":"https://forkify-api.herokuapp.com/images/fruitpizza9a19.jpg",
        "title":"Cauliflower Pizza Crust (with BBQ Chicken Pizza)",
        "id":"5ed6604591c37cdc054bcc13",
    },
   2:{
        "publisher":"A Spicy Perspective",
	    "image_url":"http://forkify-api.herokuapp.com/images/IMG_4351180x1804f4a.jpg",
        "title":"Greek Pizza",
        "id":"5ed6604591c37cdc054bca3b",
    }
    # Add more recipes here
}
    


@app.route("/recipes")
def get_recipes():
    return jsonify(recipes)

@app.route("/recipes/<string:recipe_id>")
def get_recipes_by_id(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({"error": "Recipe not found"}), 404

fall_recipes = {
    "status":'success',
    "results":3,
    "data": {"recipe": recipes}
}

@app.route("/fall_recipes")
def get_x():
    return jsonify(fall_recipes)


if __name__ == "__main__":
    app.run(debug=True)
