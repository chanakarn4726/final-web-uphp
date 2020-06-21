from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)


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

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/checkauth ", methods=['GET','POST'])
def checkauth():
    if request.method == 'POST':
        admin = request.form['admin']
        root = request.form['root']
        if admin == "admin" and root == "root":
            return render_template(url_for('edit'))
        else:
            return render_template(url_for('login'))


@app.route("/edit")
def edit():
   return render_template('edit.html')

# @app.route("/#")
#def #():
#   return render_template('#.html')

# @app.route("/#")
#def #():
#   return render_template('#.html')

# @app.route("/#")
#def #():
#   return render_template('#.html')


    
# Debug Code
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
