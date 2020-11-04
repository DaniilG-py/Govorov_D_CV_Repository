import os
import telebot as tb
from management import config, markups, text_messages



# Получение Токена телеграмм из переменной окружения(для деплоя)
# bot = tb.TeleBot(os.getenv('TG_TOKEN'))

bot = tb.TeleBot(config.TG_TOKEN)
print('Bot has been Started')


@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text:
        bot.send_message(
                        message.chat.id,
                        text_messages.HELLO_TEXT,
                        reply_markup=markups.start_keyboard(),
            )


# Выбор категории товара, либо переход в корзину
@bot.message_handler(commands=['StartShopping!'])
def category_choise(message):
    if message.text == '/StartShopping!':
        bot.send_message(
                        message.chat.id,
                        text_messages.CHOOSE_CAT_TEXT,
                        reply_markup=markups.category_choise_markup(),
            )


# Показ товара по выбранной категории, или переход в корзину
@bot.message_handler(content_types=['text'])
def show_products_by_category(message):
    if message.text == 'Перейти в корзину':
        show_cart(message.chat.id)
        return
    if message.text == 'Животные':
        cat_code = 1
    elif message.text == 'Мебель':
        cat_code = 2

    try:
        if cat_code:
            products_info = markups.send_products_by_cat(cat_code)

            for product in products_info:
                markup = markups.add_to_cart_callback(product[0])
                bot.send_photo(message.chat.id, product[3])
                bot.send_message(
                                message.chat.id,
                                f'{product[1]}  цена: {str(product[2])}',
                                reply_markup=markup,
                )
    except UnboundLocalError:
        pass


# Слушает кнопки callback для добавления в корзину или очистки корзины
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    if call.data == str(call.from_user.id):
        markups.delete_cart(call.from_user.id)
        bot.send_message(call.from_user.id, text_messages.CART_IS_EMPTY)
    else:
        markups.send_to_cart(call.from_user.id, call.data)


# Отправка пользователю его корзины
def show_cart(chat_id):
    try:
        empty_cart_callback = markups.delete_cart_callback(chat_id)

        customer_cart = markups.show_customers_cart(chat_id)
        if customer_cart[0] and customer_cart[1] != 0:
            bot.send_message(chat_id, text_messages.IN_YOUR_CART)

            product_list = ''
            for item, quantity in customer_cart[0].items():
                product_list += f'{item} - {quantity} шт.\n'

            bot.send_message(chat_id, f'{product_list}')
            bot.send_message(chat_id, f'Стоимость покупок: {customer_cart[1]} у.е.', reply_markup=empty_cart_callback)
        else:
            bot.send_message(chat_id, text_messages.CART_IS_EMPTY)
    except:
        bot.send_message(chat_id, text_messages.CHATID_NOT_FOUND)



if __name__ == '__main__':
    bot.infinity_polling(True)
