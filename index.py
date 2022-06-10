from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromedriver")

products=[]#untuk menyimpan nama produk
prices=[]#untuk menyimpan harga produk
driver.get("https://www.flipkart.com/search?q=komputer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_4ddWXP'}):
    name=a.find('a', attrs={'class':'s1W9rs'})
    price=a.find('div', attrs={'class':'_30jeq3'})
    products.append(name.text)
    prices.append(price.text)

