import logging

from src.logic.scrapper import StatsScrapper
from src.constants import PLAYERS


class Logic(object):

    def __init__(self):
        self.parser = StatsScrapper()

    def get_results(self, hero):
        results = []
        for key, value in PLAYERS.items():
            logging.info("LOGIC: Getting value for {}".format(value))
            result = self.parser.get_stats(value, hero)
            result['player'] = key
            results.append(result)

        return results
