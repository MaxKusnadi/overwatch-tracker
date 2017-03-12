import logging

from flask import Flask

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object('config')

import src.views
