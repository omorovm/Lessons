import requests
from bs4 import BeautifulSoup
html = requests.get("https://www.wikipedia.org/").text
page = BeautifulSoup(html, "lxml")
language = page.find("div", class_= "central-featured-lang lang5").find("strong").text
num = page.find("div", class_= "central-featured-lang lang5").find("bdi").text
articel = page.find("div", class_= "central-featured-lang lang5").find("span").text
print(language+"\n")
print(num, articel)