import requests
from bs4 import BeautifulSoup
import csv



CSV_1 = 'pritochnaya_vent.csv'
CSV_2 = 'air_dryer.csv'

HOST = 'https://www.rusklimat.ru'
URL_1 = 'https://www.rusklimat.ru/nijniy-novgorod/ventilyatsiya/bytovaya-pritochnaya/?COUNT=100'
URL_2 = 'https://www.rusklimat.ru/nijniy-novgorod/osushiteli/osushiteli-vozdukha-i-sushilnye-kompleksy/osushiteli_dlya_basseynov/?COUNT=100'
HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    }


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-line')
    product_cards = []

    for item in items:
        try:
            title = item.find('div', class_='ttl').get_text(strip=True)
        except:
            title = 'Наименования нет'
        prod_char = item.find_all('p', class_='char-tl')
        prod_char_inf = item.find_all('p', class_='char-in')
        prod_char_list = []
        prod_char_inf_list =[]
        for char in prod_char:
            prod_char_list.append(char.text)
        for char_inf in prod_char_inf:
            prod_char_inf_list.append(char_inf.text)
        product_info_combiner = list(zip(prod_char_list, prod_char_inf_list))
        product_info_out = [x + ' : ' + y for x, y in product_info_combiner]

        try:
            price = item.find('div', class_='curr').get_text(strip=True)
        except:
            price = 'Стоимость не найдена'
        try:
            product_link = HOST + item.find('div', class_='ttl').find('a').get('href')
        except:
            product_link = 'Ссылка не найдена'
        try:
            image_link = HOST + item.find('div', class_='cln-inf').find('img').get('data-src')
        except:
            image_link = 'Изображения нет'

        product_cards.append({
                    'title':title,
                    'product_info':product_info_out,
                    'price':price,
                    'product_link':product_link,
                    'image_link':image_link,
                })

    return product_cards


def csv_saver(product_cards, path):
    print(f'Запись в {path}')
    with open(path, 'w', newline='') as result_csv:
        writer = csv.writer(result_csv, delimiter=';')
        writer.writerow([
                        'Продукт',
                        'Характеристика',
                        'Стоимость',
                        'Ссылка на продукт',
                        'Ссылка на изображение',
                    ])

        for product in product_cards:
            writer.writerow([
                product['title'],
                product['product_info'],
                product['price'],
                product['product_link'],
                product['image_link'],
                ])


def main():
    print('Подключение к сайту...')
    html_1 = get_html(URL_1)
    if html_1.status_code == 200:
        parsing_result_1 = []
        parsing_result_1.extend(get_content(html_1.text))
        csv_saver(parsing_result_1, CSV_1)

    html_2 = get_html(URL_2)
    if html_2.status_code == 200:
        parsing_result_2 = []
        parsing_result_2.extend(get_content(html_2.text))
        csv_saver(parsing_result_2, CSV_2)

    print('Парсинг завершен')


if __name__ == '__main__':
    main()
