from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/blog_details")
def blog_details():
    return render_template('blog_details.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/elements")
def elements():
    return render_template('elements.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')
app.run(debug=True)