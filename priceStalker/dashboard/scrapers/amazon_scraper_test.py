import unittest
import warnings
from scraper import Scraper


class TestAmazonProductScraper(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=DeprecationWarning)

    def test_get_product_price(self):
        # Test scraping an amazon product's price
        url = 'https://www.amazon.com/AOC-U2790VQ-3840x2160-Frameless-DisplayPort/dp/B07LBM2DCC/ref=pd_rhf_se_p_img_10?_encoding=UTF8&psc=1&refRID=Q4E347Q2WW3WKJJSF5RZ'
        priceSelector = 'span#priceblock_saleprice, span#priceblock_ourprice, span#priceblock_dealprice'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), 0)
        url = 'https://www.amazon.com/dp/B074PK4R2H/ref=psdc_1292115011_t2_B07LBM2DCC'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), '263.00')
        # Has 'See price in cart' instead of actual price
        url = 'https://www.amazon.com/Xbox-All-Digital-Console-Disc-Free-Gaming/dp/B07XQXZXJC/ref=sr_1_1?keywords=xbox&qid=1584756939&s=electronics&sr=1-1'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), '174.95')
        url = 'https://www.amazon.com/YI-Waterproof-Surveillance-Detection-Deterrent/dp/B01CW49AGG/ref=zg_bs_photo_home_2?_encoding=UTF8&psc=1&refRID=5P9471P94RVGPXPFEBDT'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), '45.88')
        url = 'https://www.amazon.com/LORGDFDF-Microphone-Creative-Integrated-Bluetooth/dp/B0851WN4RG/ref=sr_1_1?keywords=howl+conference&qid=1584773845&s=electronics&sr=1-1'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), '113.75')
        url = 'https://www.amazon.com/Generation-Dell-Corei7-9750H-GeForce-InfinityEdge/dp/B07T3FWD22/ref=sr_1_1?keywords=xps&qid=1584773944&s=electronics&sr=1-1'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), 0)
        url = 'https://www.amazon.com/PlayStation-Portable-Core-PSP-1000-sony/dp/B000F2DE8S/ref=sr_1_10?keywords=psp&qid=1584774683&s=electronics&sr=1-10'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), 0)
        url = 'https://www.amazon.com/AmazonBasics-Pound-Neoprene-Dumbbells-Weights/dp/B01LR5RO5U?ref_=ast_sto_dp&th=1&psc=1'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), 0)
        url = 'https://www.amazon.com/Primitives-Kathy-Sign-3-Inch-Love/dp/B00HU7WRZC/ref=bbp_bb_5e8416_st_8174_w_0?psc=1&smid=ATVPDKIKX0DER'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), '6.43')
        url = 'https://www.amazon.com/dp/B07PWCWQ4Z/ref=cm_gf_aagc_iaaa_d_p0_qd0____________________cYfsB7BVGRjKYIoPUijy'
        scraper = Scraper(url)
        self.assertEqual(scraper.getProductPrice(priceSelector), '35.99')

