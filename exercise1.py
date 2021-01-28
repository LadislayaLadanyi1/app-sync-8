from flask import Flask, request

app = Flask("exercise 1")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = [ "POST" ])
def login():
    # handle the login request here
    pass

app.run()
