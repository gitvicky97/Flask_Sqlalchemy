import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Cats(db.Model):
    _tablename_ ='cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(100))
    price = =db.column(db.Integer)
    breed = db.Column(db.String(100))
    
