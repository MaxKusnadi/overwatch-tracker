import urllib.request
import logging

from bs4 import BeautifulSoup


class StatsScrapper(object):

    def __init__(self):
        self.link = "https://www.overbuff.com/players/pc/{tag}/heroes/{hero}"
        self.competitive_link = self.link + "?mode=competitive"

    def get_stats(self, tag, hero, mode="quick"):
        logging.info(
            "Getting {} information of {} for {}".format(mode, hero, tag))
        link = self.link.format(
            tag=tag, hero=hero) if mode == "quick" else self.competitive_link.format(tag=tag, hero=hero)
        logging.info("Link: {}".format(link))
        resp = urllib.request.urlopen(link)
        soup = BeautifulSoup(resp, 'html.parser')
        stats = self._parse_stats(soup, hero, mode)
        return stats

    def _parse_stats(self, soup, hero, mode='quick'):
        _class = 'player-hero theme-hero theme-hero-' + hero
        divs = soup.find(
            'div', {'class': _class})
        dic = {}
        if not self._is_hero_played(divs):
            logging.error("Quick hero is not found")
            return dic
        if mode != 'quick':
            if not self._is_hero_played_comp(divs):
                logging.error("Comp hero is not found")
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
                    except Exception:
                        pass

        return dic

    def _is_hero_played(self, divs):
        return divs

    def _is_hero_played_comp(self, divs):
        comp_div = divs.find_all('div', {"class": 'label'})
        lst_word = map(lambda x: x.text, comp_div)
        words = " ".join(list(lst_word))
        return words.find("Quick") == -1
