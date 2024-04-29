
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def about():
    return "<h2> About our class </h2>"

@app.route("/register")
def register():
    return """<h2> Inscription </h2>
                < input type="text" placeholder= votre nom svp/>
            """
@app.route("/Login")
def login():
    return render_template("login.html")

                       
         


