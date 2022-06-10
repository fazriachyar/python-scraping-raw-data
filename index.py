from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/home/fazriachyar/.wdm/drivers/chromedriver/linux64/100.0.4896.60/chromedriver")

products=[]#untuk menyimpan nama produk
prices=[]#untuk menyimpan harga produk
driver.get("https://webscraper.io/test-sites/e-commerce/allinone")#url website yang akan di scrape

content = driver.page_source#mengambil data page_source dari variabel driver
soup = BeautifulSoup(content)#mulai scrapping variabel content
# unordered_list = soup.find('div', {'class':'caption'})
# children = unordered_list.findChildren()
# for child in children:
#     print(child)

for a in soup.findAll('div', {'class':'caption'}):#temukan semua div yang memiliki class caption
    name=a.find('a', {'class':'title'})#temukan semua a yang memiliki class title
    price=a.find('h4', {'class':'pull-right price'})#temukan semua h4 yang memiliki class pull-right price
    products.append(name.text)#memasukkan data name hasil scrape ke dalam list product
    prices.append(price.text)#memasukkan data price hasil scrape ke dalam list prices

df = pd.DataFrame({'Product Name':products,'Price':prices})#membuat kolom Product Name yang berisi isi dari list products dan kolom Price yang berisi variabel prices
df.to_csv('products.csv', index=False, encoding='utf-8')#import data dalam bentuk .csv