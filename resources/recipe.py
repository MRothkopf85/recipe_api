from flask_restful import Resource, request, reqparse
from flask import jsonify, Flask
from models.recipe import RecipeModel
from sqlalchemy import JSON
import requests
import json


class Recipe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('ingredients',
                        type=JSON,
                        required=True
                        )
    parser.add_argument('directions',
                        type=str,
                        required=True)

    def post(self, name):
        # if recipes[name]["name"] == name:
        #     return {'message': "A recipe with the name '{}' already exists.".format(name)}, 400
        # json_string = request.get_json()
        # data = json.loads(json_string)
        # print(data)

        # recipe = RecipeModel.(data['name'], data['ingredients'], data['directions'])
        # recipe = RecipeModel.find_by_name(name)



        # return data
        # return requests.post('http://127.0.0.1:5000/recipe/, json={
        #     "name": name,
        #     "ingredients": ingredients,
        #     "directions": directions
        # } )

        data = Recipe.parser.parse_args()
        ingredient_list = json.dumps(data['ingredients'])
        print(type(data))
        print(data)
        # recipe = RecipeModel(name, data['ingredients'], data['directions'])
        # # print(recipe)
        # # print(recipe.json(name))
        # # print(recipe.save_to_db())
        # print(RecipeModel["ingredients"])
        # if RecipeModel.find_by_name(name):
        #     return {"message": "A recipe with that name already exists."}
        # # return recipe.json(name)
        #
        # try:
        #     recipe.save_to_db()
        # except:
        #     return {"message": "Something went wrong when adding your recipe."}, 500

        # recipes[name] = {'name': name, 'ingredients': data[name]['ingredients'], "directions": data[name]['directions']}
        # return recipe[name], 201

    def get(self, name):
        recipe = RecipeModel.find_by_name(name)
        if recipe:
            return recipe.json(name)
        return {'message': "There does not seem to be a recipe for that yet."}, 404

    def delete(self, name):
        for recipe in recipes:
            try:
                if recipes[name]["name"] == name:
                    del recipes[name]
                    return {"message": "The recipe for {} has been deleted.".format(name)}
            except:
                return {'message': "There does not seem to be a recipe for that yet."}

    def put(self, name):
        pass
