from bs4 import BeautifulSoup
import requests


class Scrapper:
    def __init__(self, link):
        self.link = link
        self.availability = self._availability_check()

    def _availability_check(self):
        req = requests.get(self.link)
        soup = BeautifulSoup(req.text, 'html.parser')

        try:
            avail = soup.find('div', class_='product-availability').text
        except AttributeError:
            print('Product page not reachable')
            return False

        if 'non disponibile' in avail.lower():
            return False
        else:
            return True


    def __str__(self):
        add = 'NOT '
        if self.availability:
            add = ''
        return f"This product is {add}available:\n{self.link}\n"



