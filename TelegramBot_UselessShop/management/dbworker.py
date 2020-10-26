import sqlite3



class DbWorker:
    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread=False)
        self.curs = self.conn.cursor()


    # Получение категорий товаров
    def get_product_types(self):
        with self.conn:
            return self.curs.execute('SELECT product_type FROM product_types').fetchall()


    # Получение Названия, Стоимости, Фотографии товара по выбранной категории
    def get_products_by_cat(self, cat_code):
        with self.conn:
            name_price_photo = self.curs.execute(f'''
                        SELECT pt.id,
                                pt.product_name,
                                pt.price,
                                pp.telegram_photo_id
                                FROM product_table pt
                                JOIN product_photos pp
                                ON pt.product_photo_id = pp.id
                                WHERE pt.product_type_id = {cat_code}''').fetchall()

            return name_price_photo


    # Добавление товара в корзину
    def add_to_cart(self, customer_id, product_id):
        with self.conn:
            self.curs.execute(f'INSERT into cart (customer_id, product_id) VALUES ({customer_id}, {product_id})')


    # Получение состава корзины по id пользователя
    def get_prod_details_from_cart(self, chat_id):
        with self.conn:
            product_names = self.curs.execute(f'''SELECT pt.product_name
                                                        FROM product_table pt
                                                        JOIN cart
                                                        ON cart.product_id = pt.id
                                                        WHERE customer_id = {chat_id}''').fetchall()
            product_prices = self.curs.execute(f'''SELECT pt.price
                                                        FROM product_table pt
                                                        JOIN cart
                                                        ON cart.product_id = pt.id
                                                        WHERE customer_id = {chat_id}''').fetchall()
            return product_names, product_prices


    # Очистка корзины пользователя
    def delete_users_cart(self, chat_id):
        with self.conn:
            self.curs.execute(f'DELETE FROM cart WHERE customer_id = {chat_id}')
        with self.conn:
            self.conn.execute('VACUUM')
