import urllib.request
from bs4 import BeautifulSoup


class StatsScrapper(object):

    def __init__(self):
        self.link = "https://www.overbuff.com/players/pc/{tag}/heroes/{hero}"

    def get_stats(self, tag, hero):
        link = self.link.format(tag=tag, hero=hero)
        resp = urllib.request.urlopen(link)
        soup = BeautifulSoup(resp, 'html.parser')

        stats = self.parse_stats(soup)
        return stats

    def _parse_stats(self, soup):
        divs = soup.find('div', {'class': 'player-hero'})
        dic = {}
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
                    except:
                        pass
        name_div = divs.find('div', {'class': 'name'})
        dic['name'] = name_div.a.text
        return dic

if __name__ == '__main__':
    s = StatsScrapper()
    r = s.get_stats("MaxKusnad-1427", "soldier76")
    print(r)
