from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


# Now this script or any imported module can use any part of Django it needs.
from dashboard import models

scraper = Scraper('amazon.com?V=owiurowieurowioeurowi',
                  'span#blah', 'img.blah-class')
price = scraper.getProductPrice()


class Scraper:
    def __init__(self, url, priceSelector, imgSelector):
        self.url = url
        self.priceSelector = priceSelector
        self.imgSelector = imgSelector
        self.userAgent = userAgent().chrome
        self.headers = {
            'User-Agent': userAgent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'If-Modified-Since': 'Mon, 18 Jul 2016 02:36:04 GMT',
            'If-None-Match': 'c561c68d0ba92bbeb8b0fff2a9199f722e3a621a',
            'Cache-Control': 'max-age=0'
        }

    def getProductPrice(self):
        price = getSoup().select("'" + self.priceSelector + "'")
        return price

    def getProductImage(self):
        image = getSoup().select("'" + self.imgSelector + "'")
        return image

    def _getSoup(self):
        return BeautifulSoup(getRequestResponse().text, 'lxml')

    def _getRequestResponse(self):
        return requests.get(self.url, headers=self.headers)
