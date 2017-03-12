from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired
from src.constants import HEROES


class SearchForm(Form):
    CHOICES = list(map(lambda x: (x[1], x[0]), HEROES.items()))
    hero = SelectField("Heroes List", choices=CHOICES,
                       validators=[DataRequired()])
