#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:57:32 2021

@author: pepe
"""

from flask import Flask, request, jsonify

app = Flask("example")

@app.route("/login", methods = ["POST"])
def handle_form_submission():
    
    print("the username is " + request.form["username"])
    
    return jsonify(request.form)

app.run()