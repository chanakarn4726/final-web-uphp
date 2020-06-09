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

    
# Debug Code
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=8000)