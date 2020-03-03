import requests
from bs4 import BeautifulSoup
import re
import time
import matplotlib.pyplot as plt
import datetime


def hello():
    print('Hello Word')

url = input('Insira aqui a URL completo do produto Amazon especifico.\n')
header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
page = requests.get(url, headers=header)
html_soup = BeautifulSoup(page.text, 'html.parser')

prices = []
dates = []
plt.show()


def check_price():
    title = html_soup.find(id='productTitle').get_text()
    price = html_soup.find(id='price_inside_buybox').get_text()
    CleanTitle = re.sub(r'(\s+|\n)', ' ', title)
    CleanPrice = re.sub(r'(\s+|\n)', ' ', price)
    UltraCleanPrice = CleanPrice[3:] 
    SuperUltraCleanPrice = UltraCleanPrice.replace('.','')
    SuperUltraCleanPrice2 = float(SuperUltraCleanPrice.replace(',','.'))
    prices.append(SuperUltraCleanPrice2)
    
    dates.append(datetime.datetime.now())
    
    print(CleanTitle)
    print(prices)
    print(dates)
    plt.suptitle(CleanTitle)
    plt.plot(dates, prices)
    plt.savefig(CleanTitle[0:10] + '.png')
    plt.pause(0.05)


    

while(True):
    check_price()
    time.sleep(60*60)
    


