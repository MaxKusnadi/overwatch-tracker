import logging

from multiprocessing.dummy import Pool
from src.logic.scrapper import StatsScrapper
from src.constants import PLAYERS


class Logic(object):

    def __init__(self):
        self.parser = StatsScrapper()

    def get_results(self, hero, mode="quick"):
        pool = Pool(5)
        results = list(pool.map(lambda key: self._parse_items(key[0], key[1], hero, mode), PLAYERS.items()))
        results = list(filter(lambda x: x, results))
        return results

    def _parse_items(self, key, value, hero, mode):
        logging.info("LOGIC: Getting value for {}".format(value))
        result = self.parser.get_stats(value, hero, mode)
        logging.info("Result from logic:")
        logging.info(result)
        if result:
            result['player'] = key
            return result
        return None
