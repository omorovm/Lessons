import requests
from bs4 import BeautifulSoup as BS
source = requests.get("http://www.example.com/").text
page = BS(source, 'lxml')
h1 = page.find("h1").text
p = page.find("p").text
a = page.find("a").get("href")
print(f'''h1: {h1}

p: {p}

a: {a}''')