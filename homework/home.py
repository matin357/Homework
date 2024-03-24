from flask import *
from flask_sqlalchemy import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///documents.db"
db = SQLAlchemy(app)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    Food_made = db.relationship('Food', backref='product')

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namme = db.Column(db.String(50), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)




@app.route("/", method="GET")
def home():
    name = request.args.get('name')
    company = Food.query.filter_by(name=name).first()
    if company:
        food = company.product
        return jsonify({
            'name of food': food.namme,
            'name of company': company.name
        })
    else:
        return jsonify({'error': 'Food is not found'}), 404




def fill_database():
    data = [
        {"name":"Nestle", "food":"childrens", "food2":"cacao"},
        {"name": "Nescafe", "food":"coffe", "food2": "more coffe"},
    ]
    for pair in data:
        compani = Company(name=pair["name"])
        db.session.add(compani)
        foood = Food(namme=pair["food"], product=compani)
        db.session.add(foood)
        try:
            post2 = Food(namme=pair["food2"], product=compani)
            db.session.add(post2)
        except KeyError:
            continue
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        fill_database()
    app.run(debug=True)