from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/home/fazriachyar/.wdm/drivers/chromedriver/linux64/100.0.4896.60/chromedriver")

products=[]#untuk menyimpan nama produk
prices=[]#untuk menyimpan harga produk
driver.get("https://webscraper.io/test-sites/e-commerce/allinone")

content = driver.page_source
soup = BeautifulSoup(content)
# unordered_list = soup.find('div', {'class':'caption'})
# children = unordered_list.findChildren()
# for child in children:
#     print(child)

for a in soup.findAll('div', {'class':'caption'}):
    name=a.find('a', {'class':'title'})
    price=a.find('h4', {'class':'pull-right price'})
    products.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')