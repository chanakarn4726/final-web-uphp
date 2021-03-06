from flask import Flask
from flask import render_template, request, redirect, url_for, session, g
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config[SQLALCHEMY_DATABASE_URI] = 'sqlite3:////home/sshuser/final-web-uphp/data.db'

db.SQLAlchemy(app)


class home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    dis = db.Column(db.String(500))
    image = db.Column(db.LargeBinary)
    date = db.Column(db.DateTime, default=datetime.now)


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User : {self.username}>'


users = []
users.append(User(id=1, username='admin', password='root'))
users.append(User(id=2, username='root', password='admin123'))

# Home Page
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/departments")
def departments():
    return render_template('departments.html')


@app.route("/doctors")
def doctors():
    return render_template('doctors.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/elements")
def elements():
    return render_template('elements.html')


@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/single-blog")
def singleblog():
    return render_template('single-blog.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['admin']
        password = request.form['root']

        user = [x for x in users if x.username == username][0]
        print(user)
        if user and user.password == password:
            # session['user_id'] == user.id

            return redirect(url_for('edit'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route("/edit")
def edit():
    return render_template('edit.html')

# @app.route("/#")
# def #():
#   return render_template('#.html')

# @app.route("/#")
# def #():
#   return render_template('#.html')

# @app.route("/#")
# def #():
#   return render_template('#.html')


# Debug Code
if __name__ == "__main__":
    # db.creat_all()
    app.debug = True
    app.run(host='0.0.0.0', port=80)
