from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def root():
    recipe_page_list=[
        ("http://127.0.0.1:5000/sage_biscuits/", "Sage Honey Butter Biscuits"),
        ("http://127.0.0.1:5000/oregano_chicken/", "Baked Chicken Topped with Cashew and Oregano Pesto"),
        ("http://127.0.0.1:5000/cashew_chicken_salad/", "Cashew Chicken Salad"),
    ]
    return render_template("root_template.html", recipe_page_list=recipe_page_list)


@app.route("/sage_biscuits/")
def sage_biscuits():
    page_title="Sage Honey Butter Biscuits"
    picture=[
        "http://2.bp.blogspot.com/-v5N-ifZ-ORc/T0fceQRuoAI/AAAAAAAADeA/RchijA7Xk3w/s1600/_MG_8036.JPG",
        "Picture of Sage Honey Biscuits"
    ]
    ingredients_list=[
        "1 cup flour",
        "1 1/2 tsp baking powder",
        "3/8 tsp salt",
        "4 tb (1/4 cup) melted salted butter",
        "1/3 cup water and honey (about 2:1)",
        "~1 tb chopped sage",
    ]
    directions_list=[
        "Preheat the oven to 450 F.",
        "Mix all ingredients, and knead for 30 seconds.",
        "Pull off small pieces of dough, then squish them so that they're about 1/4\" thick and the diameter of a 50 cent piece.Then plop them onto an ungreased cookie sheet.",
        "Bake for 5 mins, or until the biscuits are golden brown.",
        "Take the bicuits out of the oven, and immediately transfer them to a cooling rack to avoid burnt bottoms.",
        "Enjoy!",
    ]
    inspiration_and_resources_list=[
        ("http://www.thelovelyside.com/2013/03/easy-no-egg-no-milk-biscuits.html?m=1</p", "The Lovely Side: Easy No Egg, No Milk Biscuits"),
    ]
    return render_template("recipe_template.html", page_title=page_title, picture=picture, ingredients_list=ingredients_list, directions_list=directions_list, inspiration_and_resources_list=inspiration_and_resources_list)



@app.route("/oregano_chicken/")
def oregano_chicken():
    page_title="Baked Chicken Topped with Cashew and Oregano Pesto"
    picture=[
        "http://www.dinner-mom.com/wp-content/uploads/2013/05/Herb-crusted-chicken-031.jpg",
        "Picture of Baked Chicken Topped with Cashew and Oregano Pesto"
    ]
    ingredients_list=[
        "chicken tenders (or tender-sized pieces)",
        "fresh oregano",
        "shredded parmesan",
        "cashews",
        "olive oil",
    ]
    directions_list=[
        "Preheat oven to 350 F.",
        "To make the pesto, add the oregano, cashews and parmesan to a food processor and blend well. After those 3 ingredients are finely chopped, mix in enough olive oil by hand so that the other ingredients clump together.", 
        "Cover the bottom of a large baking dish with olive oil, and mix in a teaspoon or so of the pesto. Place chicken in a single layer on the bottom, flipping it in the oil to coat all sides.",
        "Bake the chicken for 15 minutes. Then take it out, flip each piece, and then top them all with a layer of pesto. Bake for an additional 10-15 minutes, or until cooked through.",
        "Enjoy!",
    ]
    inspiration_and_resources_list=[
        ("", "I searched online for what to do with tons of oregano, and someone along the way mentioned that pesto could be made with any herb. So I attempted to make an oregano pesto with ingredients I had on hand, and this is what came out of it.")
    ]
    
    return render_template("recipe_template.html", page_title=page_title, picture=picture, ingredients_list=ingredients_list, directions_list=directions_list, inspiration_and_resources_list=inspiration_and_resources_list)


@app.route("/cashew_chicken_salad/")
def cashew_chicken_salad():
    page_title="Cashew Chicken Salad"
    picture=[
        "http://www.cheeriosandlattes.com/wp-content/uploads/2012/05/IMG_1077-467x364.jpg",
        "Picture of Cashew Chicken Salad"
    ]
    ingredients_list=[
        "chicken tenders (or tender-sized pieces)",
        "balsamic vinegarette",
        "romaine",
        "tomatoes",
        "canned artichoke hearts",
        "crumbled feta",
        "cashews",
    ]
    directions_list=[
        "To make the chicken, preheat the oven to 350 F. Fill the bottom 1/4\" of a large baking dish with balsamic vinegarette. Place the chicken in a single layer on the bottom, flipping each piece in the dressing as you go to coat all sides. Then bake the chicken for 25-30 minutes, flipping it halfway through.",
        "While the chicken cooks, chop the romaine, tomatoes, canned artichoke hearts, and cashews--the smaller the better.",
        "After the chicken comes out of the oven, chop that, too.",
        "If you plan to eat the entire salad right away, combine all ingredients (including more balsamic vinegarette straight from the bottle), and serve. BUT for an even better tasting salad, combine everything except the cashews, and let the mixture sit in the fridge for a couple of hours (or overnight) to give the flavors more time to blend. Only add the cashews just before you are ready to serve, as over time they absorb moisture from the other ingredients and become mushy and flavorless.",
        "Enjoy!",
    ]
    inspiration_and_resources_list=[
        ("", "The Gordon Biersch in Palo Alto used to make such a delicious chicken cashew salad that it inspired me to try to replicate it at home!")
    ]
    
    return render_template("recipe_template.html", page_title=page_title, picture=picture, ingredients_list=ingredients_list, directions_list=directions_list, inspiration_and_resources_list=inspiration_and_resources_list)

if __name__ == "__main__":
    app.run()




