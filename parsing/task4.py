import requests
from bs4 import BeautifulSoup as BS

def getTitle(url):
    html = requests.get(url).text
    title = BS(html, "lxml")
    h1 = title.find("h1")
    if h1 == None:
        return "Title could not be found"
    return h1.text

print(getTitle('http://www.example.com/'))
