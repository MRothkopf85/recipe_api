from flask_restful import Resource, request
from models.recipe import RecipeModel


class Recipe(Resource):
    def post(self, name):
        # if recipes[name]["name"] == name:
        #     return {'message': "A recipe with the name '{}' already exists.".format(name)}, 400
        # data = request.get_json()
        # print(data)
        print(name)
        #
        # if RecipeModel.find_by_name(name):
        #     return {"message": "A store with that name already exists."}
        # recipe = data[name]
        # try:
        #     recipe.save_to_db()
        # except:
        #     return {"message": "Something went wrong when adding your recipe."}, 500
        #
        # recipes[name] = {'name': name, 'ingredients': data[name]['ingredients'], "directions": data[name]['directions']}
        # # return recipes[name], 201

    def get(self, name):
        recipe = RecipeModel.find_by_name(name)
        if recipe:
            return recipe.json()
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
