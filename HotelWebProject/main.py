from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'

app.config['SECRET_KEY'] = 'thisisamyveryverysecret'
db = SQLAlchemy(app)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/contact', methods=['Get', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form["txtName"]
            email = request.form["txtEmail"]
            phone = request.form["txtPhone"]
            message = request.form["txtMsg"]

            entry = Client(name=name, email=email, phone=phone, message=message)

            db.session.add(entry)
            db.session.commit()
            return redirect('/home')
        except:
            return redirect('/')

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
