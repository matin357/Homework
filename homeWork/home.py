from flask import *

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # binding DB and Flask App

names=""


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    whroting = db.Column(db.String(5000), nullable=False)



@app.route("/")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False)