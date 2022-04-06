from bs4 import BeautifulSoup
import requests
import lxml

url="https://www.amazon.it/Justice-All-Metallica/dp/B07GX5PVZF/ref=sr_1_7?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9KJ7G8XO37D&keywords=vinile+metallica&qid=1649046214&sprefix=vinile+metallica%2Caps%2C109&sr=8-7"

r=requests.get(url=url, headers={"Accept-Language":"it,it-IT;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6,en;q=0.5","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"})

soup=BeautifulSoup(r.content, "lxml")

tags=soup.find(class_="a-offscreen")

print(float(tags.text[:-1].replace(',','.')))
