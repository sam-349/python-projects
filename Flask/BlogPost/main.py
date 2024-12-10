from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# initialize Flask
app = Flask(__name__)


# secret key
app.config['SECRET_KEY'] = '275221af80bf5fbf6dcb4fc033b84b29'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
db = SQLAlchemy(app)


# create models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # create relations
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}), {self.password}, {self.image_file}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"POST('{self.title}', {self.date_posted})) "


posts = [
    {
        "author": "john",
        "title": "blog-title1",
        "content": "blog content",
        "date_posted": "april 12, 2024"
    },
    {
        "author": "dev",
        "title": "blog-title2",
        "content": "blog content",
        "date_posted": "mar 11, 2024"
    },
]


# create a router
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "samuel@gmail.com" and form.password.data == '12345678':
            flash('You Successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please Check Username and Password', 'danger')
    return render_template("login.html", title="Login", form=form)


# run script directly by python
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
