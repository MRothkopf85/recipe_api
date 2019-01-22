'''
Receive input from user, convert that data into a Recipe object.  Then, return
a JSON string to be used by API
'''

import json

name = input("Recipe name: ")
ingredients = {}
print("Now we will enter the ingredients!  You will first be asked for the ingredient (ie Sugar) and then for the measurement (ie 1 Tbsp)")

moreIngredients = input("Would you like to enter an ingredient? y/n ")
while moreIngredients == 'y':
    x = input("Enter ingredient: ")
    y = input(" and measurement: ")
    ingredients[x] = y
    moreIngredients = input("Would you like to add another ingredient? y/n ")

directions = input("Please enter the instructions for your recipe:  ")

d = {}
d[str(name)] = {"name": name, "ingredients": ingredients, "directions": directions}

# url = 'http://127.0.0.1:5000'
# payload = d
# r = requests.post(url, json=payload)


jsonData = json.dumps(d)
print(jsonData)



# print(name)
# print(ingredients)
# print(directions)
#
# print(d)
