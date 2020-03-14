from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

# Get the most up to date chrome user agent to pass in the request
# Just so the server thinks a normal browser is making the request
url = 'https://www.amazon.com/Breitling-Transocean-Day-Date-Automatic/dp/B00HJUPQ7G?pf_rd_r=FVXQ3G5RY0V6E0MK1BQ3&pf_rd_p=700385e0-19d0-4b4c-89bf-06e23d6f1594&pd_rd_r=ea2b3f36-7f6e-4d2f-8894-270668fa847f&pd_rd_w=DPzxj&pd_rd_wg=2LGtw&ref_=pd_gw_cr_simh'
userAgentString = UserAgent().chrome
headers = {
    'User-Agent': userAgentString,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-Modified-Since': 'Mon, 18 Jul 2016 02:36:04 GMT',
    'If-None-Match': 'c561c68d0ba92bbeb8b0fff2a9199f722e3a621a',
    'Cache-Control': 'max-age=0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
