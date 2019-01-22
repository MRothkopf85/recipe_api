my_dict = {"recipe": {
    "name": "sandwich",
    "ingredients" : {
        "Bread": "2 slices",
        "Ham": "2 slices",
        "Mayo": "1 Tbsp",
        "Mustard": "1 Tbsp"
        },
    "directions": "Make sandwich"
    }
}

print(my_dict)

answer = input("What recipe are you looking for?" )

if answer == my_dict["recipe"]["name"] :
    print(my_dict)
else:
    print("There is no recipe with that name")