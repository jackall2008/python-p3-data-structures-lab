import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = []
    for food in spicy_foods:
        if 'name' in food:
            food_names.append(food['name'])
    return food_names
        

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []

    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest_foods.append(food)
    return spiciest_foods


def print_spicy_foods(spicy_foods):

    for food in spicy_foods:
        pepper_meter = food['heat_level'] * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {pepper_meter}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):

    for food in spicy_foods:
        if food['heat_level'] > 5:
            pepper_meter = food['heat_level'] * "🌶"
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {pepper_meter}")


def get_average_heat_level(spicy_foods):
    levels_of_heat = [food['heat_level'] for food in spicy_foods]

    average = sum(levels_of_heat) / len(levels_of_heat)

    return average

def create_spicy_food(spicy_foods, spicy_food):

    added_spicy_foods = [food for food in spicy_foods]
    
    added_spicy_foods.append(spicy_food)

    return added_spicy_foods
