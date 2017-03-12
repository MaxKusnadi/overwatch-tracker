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
        comp_results = logic.get_results(hero, "comp")
        keys = results[0].keys()
        comp_keys = comp_results[0].keys()
        logging.info("View:")
        logging.info(comp_results)
        logging.info("Finish scrapping..")
        return render_template('index.html', form=form,
                               hero=hero.upper(),
                               results=results,
                               keys=keys,
                               comp_results=comp_results,
                               comp_keys=comp_keys)
    return render_template('index.html', form=form, results=None)
