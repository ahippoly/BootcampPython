
cookbook = {}
quit = 0

def add_recipe(name, ingredients, meal, prep_time) :
    new_recipe = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    cookbook[name] = new_recipe
    return 1

def del_recipe(name) :
    cookbook.pop(name)

def print_recipe(name) :
    print("Recipe for cake:\n"
          + "Ingredients list: " + str(cookbook[name]["ingredients"]) + "\n"
          + "To be eaten for " + str(cookbook[name]["meal"]) + ".\n"
          + "Takes " + str(cookbook[name]["prep_time"]) + " minutes of cooking.")

def init_cookbook() :
    add_recipe("sandwich", ["ham", "bread", "cheese", "tomatoes"], "lunch", 10)
    add_recipe("cake", ["flour", "sugar", "eggs"], "dessert", 60)
    add_recipe("salad", ["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15)

def print_selection_menu() :
    print("Please select an option by typing the corresponding number:\n"
          + "1: Add a recipe\n"
          + "2: Delete a recipe\n"
          + "3: Print a recipe\n"
          + "4: Print the cookbook\n"
          + "5: Quit")

def print_wrong_selection() :
    print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")

def menu_add_recipe() :
    print("write recipe name:")
    name = input()
    print("Now write the required ingredients (write \"end\" to stop adding ingredients):")
    ingredients = []
    ingredient = ""
    while (ingredient != "end") :
        if (ingredient != "") :
            ingredients.append(ingredient)
        ingredient = input()
    print("Now write meal type")
    meal = input()
    print("Now preparation time")
    prep = None
    while prep == None :
        prep = input()
        try :
            prep = int(prep)
        except :
            prep = None
            print("please write a correct number")
    add_recipe(name, ingredients, meal, prep)
    print("recipe correctly added to cookbook")
            
def menu_del_recipe() :
    print("Write the name of the recipe to be deleted")
    name = input()
    if name in cookbook :
        cookbook.pop(name)
        print("Successfully deleted recipe")
    else :
        print("This recipe isn't in the cookbook")

def menu_print_recipe() :
    print("Write the name of the recipe you want to see")
    name = input()
    if name in cookbook :
        print_recipe(name)
    else :
        print("sorry there is no recipe with this name")

def menu_print_cookbook() :
    print("this is all the recipe contained by the cookbook")
    for recipe_name in cookbook :
        print(recipe_name)

def menu_quit() :
    print("Cookbook closed.")
    exit()

choice_fn = [0]
choice_fn.insert(1, menu_add_recipe)
choice_fn.append(menu_del_recipe)
choice_fn.append(menu_print_recipe)
choice_fn.append(menu_print_cookbook)
choice_fn.append(menu_quit)

def handle_menu_selection() :
    choice = input()
    try :
        choice = int(choice)
    except :
        choice = 0
    if choice > 0 and choice < 6 :
        choice_fn[choice]()
    else :
        print_wrong_selection()

init_cookbook()
while quit != 1 :
    print_selection_menu()
    handle_menu_selection()

