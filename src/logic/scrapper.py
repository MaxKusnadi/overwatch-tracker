import urllib.request
import logging

from bs4 import BeautifulSoup


class StatsScrapper(object):

    def __init__(self):
        self.link = "https://www.overbuff.com/players/pc/{tag}/heroes/{hero}"

    def get_stats(self, tag, hero):
        logging.info("Getting information of {} for {}".format(hero, tag))
        link = self.link.format(tag=tag, hero=hero)
        logging.info("Link: {}".format(link))
        resp = urllib.request.urlopen(link)
        soup = BeautifulSoup(resp, 'html.parser')

        stats = self._parse_stats(soup, hero)
        return stats

    def _parse_stats(self, soup, hero):
        _class = 'player-hero theme-hero theme-hero-' + hero
        divs = soup.find(
            'div', {'class': _class})
        dic = {}
        if not divs:
            return dic
        for div in divs:
            for x in div.children:
                for y in x.children:
                    try:
                        value = y.find('div', {'class': 'value'})
                        label = y.find('div', {'class': 'label'})
                        if not label.text:
                            labels = y.find_all('div', {'class': 'label'})
                            for lab in labels:
                                if lab.text:
                                    label = lab
                            dic[label.text] = value.text

                        else:
                            dic[label.text] = value.text
                    except Exception as err:
                        pass

        return dic
