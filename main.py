from bs4 import BeautifulSoup
import requests
import contextlib
import csv
from selenium import webdriver
from Prodotto import Prodotto

prodotti = []

def main():

    driver = webdriver.Chrome()

    url = "https://www.amazon.com/"
    global donny


    get_url("garden gloves")

    driver.get(get_url("garden gloves"))

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    for item in results:
        extract_record(item)
    print(len(results))

'''

    item = results[0]
    atag = item.h2.a
    print(atag.text)
    url = 'https://www.amazon.com/'+atag.get('href')
    price_parent = item.find('span', 'a-price')
    price_parent = price_parent.find('span', 'a-offscreen')
    print(price_parent.text)
    rating = item.i.text[0:3]
    print(rating)
    print(item.i.text)
    review_count = item.find('span', {'class' : 'a-size-base s-underline-text'}).text
    r1 = review_count.replace('(','')
    r1 = r1.replace(')','')
    r1 = r1.replace(',', '.')
    num1 = float(r1)


    print(num1)

'''







def extract_record(item):
    atag = item.h2.a
    titolo = atag.text
    url = 'https://www.amazon.com/' + atag.get('href')
    price_parent = item.find('span', 'a-price')
    price_parent = price_parent.find('span', 'a-offscreen')
    if price_parent.text == '':
        return
    prezzo = int(price_parent.text.replace('$', ''))
    print(price_parent.text)
    rating = int(item.i.text[0:3])
    print(rating)
    print(item.i.text)
    review_count = item.find('span', {'class': 'a-size-base s-underline-text'}).text
    r1 = review_count.replace('(', '')
    r1 = r1.replace(')', '')
    r1 = r1.replace(',', '.')
    prod = Prodotto(titolo, prezzo, url, rating, r1)
    prodotti.append(prod)

    return


def get_url(string):
    base = 'https://www.amazon.com/s?k={prodotto}&sprefix=ultrawi%2Caps%2C183&ref=nb_sb_ss_ts-doa-p_2_7'
    if " " in string:
        string = string.replace(' ', '+')
    donny = base.format(prodotto = string)
    return donny



main()

