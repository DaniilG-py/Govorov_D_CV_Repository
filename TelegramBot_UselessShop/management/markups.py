# Модуль, отвечает за конструкцию клавиатур и получение данных из БД
# для отправки их пользователю. Единственный модуль, работающий с БД.

import telebot as tb
from .dbworker import DbWorker
from .config import DATABASE
from . import cart



db = DbWorker(DATABASE)


def start_keyboard():
    markup = tb.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row('/StartShopping!')

    return markup


# Клавиатура выбора категории или перехода в корзину
def category_choise_markup():
    product_types = db.get_product_types()
    markup = tb.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row(product_types[0][0], product_types[1][0])
    markup.row('Перейти в корзину')

    return markup


# Получение товара из БД по выбранной категории
def send_products_by_cat(cat_code):
    product_list = db.get_products_by_cat(cat_code)

    return product_list


# Callback кнопка для добавления товара в корзину, в callback_data содержится id товара соответствующее id товара в БД
def add_to_cart_callback(product_id):
    markup = tb.types.InlineKeyboardMarkup()
    callback_button = tb.types.InlineKeyboardButton(text='Добавить в корзину', callback_data=str(product_id))
    markup.add(callback_button)

    return markup


# Отправка товара в корзину.
# Функция является 'транзитной', чтобы ограничить работу с БД только с этом модуле.
def send_to_cart(chat_id, product_id):
    db.add_to_cart(chat_id, product_id)


# Получение корзины пользователя, собранной в модуле 'cart'
def show_customers_cart(chat_id):
    customer_cart = cart.generate_cart_innards(db.get_prod_details_from_cart(chat_id))

    return customer_cart


# callback для очистки корзины пользователя
def delete_cart_callback(chat_id):
    markup = tb.types.InlineKeyboardMarkup()
    callback_button = tb.types.InlineKeyboardButton(text='Очистить корзину', callback_data=str(chat_id))
    markup.add(callback_button)

    return markup


# Очистка корзины пользователя
def delete_cart(chat_id):
    db.delete_users_cart(chat_id)
