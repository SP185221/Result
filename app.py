from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///result_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/show", methods=['GET', 'POST'] )
def show():
    if request.method=='POST':
        roll = request.form['RollNo']
        stds = Result.query.filter_by( roll = int(roll) )
        return render_template("result.html", stds = stds)
    else:
        return render_template("login.html")


@app.route("/add")
def add():
    data = Result(roll = 12345678, name = "Shailesh", fname = "R S Patel", mname = "L Devi" , hindi = 98, english = 97 , science = 96 , homescience = 99, socialscience = 95, drawing = 95 ) 
    db.session.add(data)
    db.session.commit()
    
    return render_template("result.html")

# Database connectivity

class Result(db.Model):
    roll = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    fname = db.Column(db.String(200), nullable=False)
    mname = db.Column(db.String(200), nullable=False)
    hindi = db.Column(db.Integer)
    english = db.Column(db.Integer)
    science = db.Column(db.Integer)
    homescience = db.Column(db.Integer)
    socialscience = db.Column(db.Integer)
    drawing = db.Column(db.Integer)

    #def __repr__(self) -> str:
        #return f"{self.sno} - {self.title}"


if __name__ == "__main__":
    app.run(debug = True , port = 8000)