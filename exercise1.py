from flask import Flask, request, render_template

app = Flask("exercise 1")

users = {
    "pepe": "p4ss",
    "rafa": "w0rd"
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = [ "POST" ])
def login():
    # check if the user and and password exists in the db
    username = request.form["username"]
    password = request.form["pass"]
    
    if username in users and users[username] == password:
        return render_template("private.html")
    else:
        return render_template("unauthorized.html")

app.run()
