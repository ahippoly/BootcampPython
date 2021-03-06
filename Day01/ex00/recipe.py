class Recipe:
    def __init__(self, name = None,
                 cooking_lvl = None,
                 cooking_time = None,
                 ingredients = None,
                 description = "", 
                 recipe_type = None):
        err = 0
        if not isinstance(name, str) :
            err = 1
            print("Name of recipe must be a string")
        if not isinstance(cooking_lvl, int) :
            err = 1
            print("cooking level must be a int")
        elif cooking_lvl > 5 or cooking_lvl < 1 :
            err = 1
            print("cooking level must be between 1 and 5")
        if not isinstance(cooking_time, int) :
            err = 1
            print("cooking time must be a int")
        elif cooking_time < 0 :
            err = 1
            print("cooking time must be a positive number, you cant gain time by cooking wtf")
        if not isinstance(ingredients, list) :
            print("ingredients must be a list a string values")
        else :
            correct = 1
            for i in ingredients :
                if not isinstance(i, str) :
                    correct = 0
            if correct == 0 :
                err = 1
                print("All ingredients must be strings")
        if not isinstance(description, str) :
            err = 1
            print("description must be a string")
        if not isinstance(recipe_type, str) :
            err = 1
            print("recipe type must be a string")
        else :
            if not (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert") :
                err = 1
                print("recipe type must be a \'starter\', a \'lunch\' or a \'dessert\'")
        if err == 0 :
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
    def __str__(self):
        """Return the string to print with the recipe info"""

        str_ingredients = "\n  - " + "\n  - ".join(self.ingredients)
        txt = ("the name of the recipe is : " + self.name 
        + "\n recipe description :\n" + self.description
        + "\n the difficulty is " + str(self.cooking_lvl)
        + "\n the cooking time is " + str(self.cooking_time)
        + "\n the ingredients required are :" + str_ingredients
        + "\n recipe type is : " + self.recipe_type)
        return txt        
