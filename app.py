import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

try:
    pguser = os.environ["POSTGRES_USER"]
    pgpass = os.environ["POSTGRES_PASS"]
    pgurl = os.environ["POSTGRES_URL"]
    pgdb = os.environ["POSTGRES_DB"]
except:
    pguser = "user"
    pgpass = "pass"
    pgurl = "postgres_db"
    pgdb = "anaconda_db"

dbconnstring = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=pguser,pw=pgpass,url=pgurl,db=pgdb)
app.config['SQLALCHEMY_DATABASE_URI'] = dbconnstring
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {"id": self.id,
                "name": self.name}

@app.route('/')
def ready():
    return "system ready"

@app.route('/item', methods=['GET', 'POST'])
def handle_items():
    if request.method == "GET":
        items = Item.query.all()
        results = [
            {
                "id": item.id,
                "name": item.name
            } for item in items]

        return {"result": results}

    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            newitem = Item(name=data['name'])
            db.session.add(newitem)
            db.session.commit()
            return {"result": f"created item {newitem.name}"}
        else:
            return {"error": "The request payload is not in JSON format"}

@app.route('/item/<id>', methods=['GET', 'PATCH', 'DELETE'])
def handle_item(id):
    item = Item.query.get_or_404(id)
    if request.method == 'GET':
        result = {
            "id": item.id,
            "name": item.name
        }
        return {"result": result}

    elif request.method == 'PATCH':
        data = request.get_json()
        item.name = data['name']
        db.session.add(item)
        db.session.commit()
        return {"result": f"item {item.id} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return {"message": f"item {item.name} successfully deleted."}


if __name__ == '__main__':
    app.run()