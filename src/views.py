import logging

from flask import render_template
from src import app
from src.forms import SearchForm
from src.logic.main import Logic
from flask import request


logic = Logic()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        hero = request.form['hero']
        results = logic.get_results(hero)
        return render_template('index.html', form=form, results=results, hero=hero)
    return render_template('index.html', form=form, results=None, hero=None)
