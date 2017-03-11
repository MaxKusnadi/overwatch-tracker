import logging


from flask import render_template
from src import app


@app.route('/', methods=['GET'])
def index():
    return "Hello world"
