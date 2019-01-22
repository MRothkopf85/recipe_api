from db import db

class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    
    name = db.Column(db.String(80), primary_key=True)
    ingredients = db.Column(db.String(300))
    directions = db.Column(db.String(300))

    def __init__(self, name):
        self.name = name
        self.ingredients = ingredients
        self.directions = directions

    def json(self, name):
        return {
            "name": self.name,
            "ingredients": self.name["ingredients"],
            "directions": self.name["directions"]
        }

    def find_by_name(self, name):
        return RecipeModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit(self)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
