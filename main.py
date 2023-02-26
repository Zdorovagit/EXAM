import requests
from bs4 import BeautifulSoup
import lxml

for i in range(1, 6):
    url = f'https://allo.ua/ua/televizory/p-{i}/proizvoditel-samsung/'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        all_product = soup.find('div', class_='products-layout__container products-layout--grid')
        products = all_product.find_all('div', class_='product-card__content')
        for product in products:
            try:
                oldprice = product.find('div', class_='v-pb__old')
                print(oldprice.text)
                newprice = product.find('div', class_='v-pb__cur discount')
                print(newprice.text)
            except Exception:
                newprice = None
                print('Это без скидки было')
            if newprice != None:
                title = product.find('a', class_='product-card__title')
                print(title.text)
                with open('analog.txt', 'a', encoding='utf-8') as file:
                    file.write(
                        f"{title.text} {oldprice.text.replace('NBSP', '')} {newprice.text.replace('NBSP', '')}" '\n')
