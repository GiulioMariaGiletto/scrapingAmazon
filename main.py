from bs4 import BeautifulSoup
import requests
import contextlib
import csv
from selenium import webdriver
from Prodotto import Prodotto

prodotti = []
global donny
global pickprod
def main():

    driver = webdriver.Chrome()
    pickprod = input(" Select a product: ")
    for page in range(1, 21):
        if page == 1:
            url = get_url(pickprod)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = soup.find_all('div', {'data-component-type': 's-search-result'})
        else:
            url = turn_page(pickprod, page)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = soup.find_all('div', {'data-component-type': 's-search-result'})




    for item in results:
        extract_record(item)
    print(len(results))

    for prod in prodotti:
        print(prod)

    return


def extract_record(item):
    if type(item) == 'NoneType':
        return
    atag = item.h2.a
    titolo = atag.text
    url = 'https://www.amazon.com/' + atag.get('href')
    try:
        price_parent = item.find('span', 'a-price')
        price_parent = price_parent.find('span', 'a-offscreen')
        prezzo = float(price_parent.text.replace('$', ''))
        print(price_parent.text)
    except AttributeError:
        return

    try:
        if item.i.text[0:3] == '':
            rating = 0.0
        else:
            rating = float(item.i.text[0:3])
    except AttributeError:
        rating = 0.0
    print(rating)

    try:
        print(item.i.text)
        review_count = item.find('span', {'class': 'a-size-base s-underline-text'}).text
        r1 = review_count.replace('(', '')
        r1 = r1.replace(')', '')
        r1 = float(r1.replace(',', '.'))
    except AttributeError:
        r1 = 0.0
    prod = Prodotto(titolo, prezzo, url, rating, r1)
    prodotti.append(prod)

    return

def sorting_product(List):
    prodotti.sort(Prodotto.punteggio)
    return


def get_url(string):
    base = 'https://www.amazon.com/s?k={prodotto}&sprefix=ultrawi%2Caps%2C183&ref=nb_sb_ss_ts-doa-p_2_7'
    if " " in string:
        string = string.replace(' ', '+')
    donny = base.format(prodotto = string)
    return donny


def turn_page(string, page):
    if " " in string:
        string = string.replace(' ', '+')
    base = 'https://www.amazon.com/s?k='+string+'&page={a}&crid=CIO0PKVSSOAI&qid=1677448063&sprefix='+string+'%2Caps%2C482&ref=sr_pg_{b}'
    newy = base.format(a = page)
    newy = newy.format(b = page)

    return newy



main()

