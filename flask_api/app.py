from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/users")
def get_users():
    users = [{"name": "Alice"}, {"name": "Bob"}]
    return jsonify(users)


@app.route("/<name>")
def print_name(name):
    return "Hi , {}".format(name) 

recipes = [
    {
        "id": 1,
        "name": "Spaghetti with Meatballs",
        "ingredients": ["spaghetti", "meatballs", "tomato sauce", "onions", "garlic"],
        "instructions": "Cook the spaghetti according to package directions. ..."
    },
{
        "id": 2,
        "name": "Seafood Spaghetti",
        "ingredients": ["spaghetti", "shrips", "tomato sauce", "onions", "garlic"],
        "instructions": "Cook the spaghetti according to package directions. ..."
    },
    # Add more recipes here
]

@app.route("/recipes")
def get_recipes():
    return jsonify(recipes)

@app.route("/recipes/<int:recipe_id>")
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({"error": "Recipe not found"}), 404

recettes = [
	{
        "publisher":"Closet Cooking",
	    "image_url":"http://forkify-api.herokuapp.com/images/BBQChickenPizzawithCauliflowerCrust5004699695624ce.jpg",
	    "title":"Cauliflower Pizza Crust (with BBQ Chicken Pizza)",
	    "id":"5ed6604591c37cdc054bcd09",
        "code":1

	},
    {
        "publisher":"Closet Cooking",
        "image_url":"http://forkify-api.herokuapp.com/images/BBQChickenPizzawithCauliflowerCrust5004699695624ce.jpg",
        "title":"Cauliflower Pizza Crust (with BBQ Chicken Pizza)",
        "id":"5ed6604591c37cdc054bcc13",
        "code":2
    },
]

@app.route("/recettes")
def get_recettes():
    return jsonify(recettes)


@app.route("/recettes/<string:recette_code>")
def get_recette(recette_code):
    recipe = next((recipe for recipe in recettes if recipe["id"] == recette_code), None)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({"error": "Recipe not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
