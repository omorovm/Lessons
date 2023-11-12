import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BS(html, "lxml")
    get_last_page(soup)
    catalog = soup.find("div", class_ = "browse-view")
    laptops = catalog.find_all('div', class_ = 'row')
    # laptop = catalog.find('div', class_ = 'row')
    for laptop in laptops:
        title = laptop.find('a', class_ = "product-image-link").get('title')
        image = laptop.find('img').get('src')

        image = f'https://enter.kg{image}'
        price = laptop.find("span", class_="price").text

        data = {
            'title': title,
            'image': image,
            'price': price
        }
        write_csv(data)
        
def get_last_page(html):
    soup = BS(html, "lxml")
    last_page = soup.find("li", class_ = "pagination-end")
    last_page = last_page.find("a").get("href")
    print(last_page)

def write_csv(data):
    with open('enter_laptops.csv', 'a') as csvfile:
        name = ['title', 'image', 'price']
        writer = csv.DictWriter(csvfile, delimiter="|", fieldnames=name)
        writer.writerow(data)


def main():
    url = "https://enter.kg/computers/noutbuki_bishkek"
    html = get_html(url)
    last_page = get_last_page(html)
    # get_data(html)
    for page in range(1, last_page + 1, 100):
        url = f"https://enter.kg/computers/noutbuki_bishkek/{page}-{page-1}"
        html = get_html(url)
        get_data(html)
main()



# for i in range(1, 1502,100):
    # f'https://enter.kg/computers/noutbuki_bishkek