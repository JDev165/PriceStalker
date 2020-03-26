from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import ast


class Scraper:
    def __init__(self, url):
        self.url = url
        self.userAgent = UserAgent().chrome
        self.headers = {
            'User-Agent': self.userAgent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'If-Modified-Since': 'Mon, 18 Jul 2016 02:36:04 GMT',
            'If-None-Match': 'c561c68d0ba92bbeb8b0fff2a9199f722e3a621a',
            'Cache-Control': 'max-age=0'
        }

    def getProductPrice(self, priceSelector):
        # Returns list so just need the first occurrence, hence price[0]
        priceElementsList = self._getSoup().select(priceSelector)
        price = 0 if len(priceElementsList) == 0 else priceElementsList[0].text.replace('$','')
        return price

    def getProductImageSrc(self, imgSelector):
        # Returns list so just need the first occurrence, hence image[0]
        imageElementsList = self._getSoup().select(imgSelector)
        imageSrc = imageElementsList[0] if len(
            imageElementsList) >= 1 else 'N/A'
        imagesDict = ast.literal_eval(imageSrc.get('data-a-dynamic-image'))
        imageSrc = next(iter(imagesDict))
        return imageSrc

    def _getSoup(self):
        return BeautifulSoup(self._getRequestResponse().text, 'lxml')

    def _getRequestResponse(self):
        return requests.get(self.url, headers=self.headers)


# def main():
    # url = 'https://www.amazon.com/Calvin-Klein-Cotton-Stretch-Multipack/dp/B00JQSZRQ4/ref=sxin_0_osp48-2dfeb0ec_cov?ascsubtag=amzn1.osa.2dfeb0ec-873d-4b26-8bfd-bb2b83bb4d8c.ATVPDKIKX0DER.en_US&creativeASIN=B00JQSZRQ4&cv_ct_cx=underwear&cv_ct_id=amzn1.osa.2dfeb0ec-873d-4b26-8bfd-bb2b83bb4d8c.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=underwear&linkCode=oas&pd_rd_i=B00JQSZRQ4&pd_rd_r=4c40b042-9291-434e-afcb-a7c6e4b376e0&pd_rd_w=hFEkI&pd_rd_wg=j1l3z&pf_rd_p=dac4d66e-658f-4cae-b10d-a35ac5eca0c3&pf_rd_r=7Y6MT4QXD5FFPT050RVD&qid=1584589707&s=electronics&tag=spyonsite-20'
    # priceSelector = 'span#priceblock_saleprice, span#priceblock_ourprice'
    # imgSelector = 'div#imgTagWrapperId img#landingImage, div#imgTagWrapperId img.a-dynamic-image'
    # scraper = Scraper(url, priceSelector, imgSelector)
    # print(scraper.getProductPrice())
    # image = scraper.getProductImageSrc()
    # imagesDict = ast.literal_eval(image.get('data-a-dynamic-image'))
    # print(next(iter(imagesDict)))


# if __name__ == "__main__":
#    main()
