# github.com/echtr
from bs4 import BeautifulSoup as bs
import requests

# scraping usage, local files
with open("index.html", "r", encoding="utf-8") as file:
	content = file.read()
	soup = bs(content, "lxml")


# find() & find_all()
tag = soup.find("h5") # sadece ilk elementi alır
tags = soup.find_all("h5") # bütün elementleri alır


# grab all prices
tags = soup.find_all("div", class_ = "card") # 'class' ı argüman olarak alamayız 
#çünkü o bir python keyword'ü, bu yüzden 'class_' olarak kullanıyoruz

#for tag in tags:
#	print(f"İsim: {tag.h5.text}\tFiyat: {tag.a.text.split()[-1]}") # her bir tag için tagde bulunan h5leri alıyoruz



# scraping a production
url = "http://books.toscrape.com/"
html_text = requests.get(url).text
soup = bs(html_text, "lxml")

isim = soup.find("article", class_="product_pod")
fiyat = soup.find("p", class_= "price_color")
print(f"İsim: {isim.h3.text}\nFiyat: {fiyat.text}")