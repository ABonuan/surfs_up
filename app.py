from flask import Flask

# create new Flask instance called "app"
app = Flask(__name__)

# define the starting point, aka "root"
@app.route("/")
def hello_world():
    return "Hello world"
