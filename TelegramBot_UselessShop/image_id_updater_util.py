import os
from time import sleep
import sqlite3
import telebot as tb


# впишите Ваш телеграм токен сюда
TG_TOKEN = '1212019016:AAFEZkLQK-b5bbVB06pkxzrgMil6da3eYKQ'

bot = tb.TeleBot(TG_TOKEN)
conn = sqlite3.connect('shop.db', check_same_thread=False)
curs = conn.cursor()


@bot.message_handler(commands=['run'])
def send_images(message):
    image_dict = {}

    for file in os.listdir('images/'):
        if file.split('.')[-1] == 'png':
            file_name = str(file.split('.')[0])

            f = open('images/'+file, 'rb')

            msg = bot.send_photo(message.chat.id, f, None)
            photo_id = msg.json['photo'][0]['file_id']
            bot.send_message(
                message.chat.id,
                photo_id,
                reply_to_message_id=msg.message_id,
            )

            image_dict.update({str(file_name): photo_id})
            sleep(0.5)

    write_id_to_db(image_dict)
    bot.send_message(
                    message.chat.id,
                    'id Изображений успешно обновлены!'
    )


# Перезапись id изображений в БД
def write_id_to_db(data):
    for name, id in data.items():
        with conn:
            curs.execute(f'UPDATE product_photos SET telegram_photo_id="{id}" WHERE product_id = {name}')


if __name__ == '__main__':
    bot.infinity_polling()
