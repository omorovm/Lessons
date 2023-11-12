import requests
from bs4 import BeautifulSoup as BS


def find_category(categories, keyword):
    list_ = [i for i in categories if keyword.lower() in i.lower()]
    return list_


html = requests.get('https://enter.kg/').text
soup = BS(html, "lxml")
category_list = [i.text for i in soup.find("div", class_= "moduletable").find_all("a")]
print(find_category(category_list, 'Ноутбуки'))