from app import app
from flask import request, redirect, render_template, url_for, flash, make_response

"""
Views for the Flask app. Contains the routes for the page routing
"""


@app.route('/')
def home():
    flash("Work in progress!", category='error')
    return render_template('home.html')

