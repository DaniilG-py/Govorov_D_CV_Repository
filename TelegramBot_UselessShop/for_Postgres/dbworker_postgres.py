import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


class DbWorker:

    def __init__(self):
        _USER_NAME = os.getenv('_USER_NAME')
        _PASSWORD = os.getenv('_PASSWORD')
        _HOST = os.getenv('_HOST')
        _PORT = os.getenv('_PORT')
        _BASE_NAME = os.getenv('_BASE_NAME')
        _HEROKU_CLI = os.getenv('_HEROKU_CLI')

        self.engine = sa.create_engine(f'postgresql://{_USER_NAME}:{_PASSWORD}@{_HOST}:{_PORT}/{_BASE_NAME}', echo=False)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.meta = sa.MetaData(bind=self.engine, reflect=True)

        # Объекты таблиц БД
        self.product_table = self.meta.tables['product_table']
        self.product_types = self.meta.tables['product_types']
        self.product_photos = self.meta.tables['product_photos']
        self.cart = self.meta.tables['cart']


    # Получение категорий товаров
    def get_product_types(self):
        product_type_list = []
        product_types = self.session.query(self.product_types.columns.product_type)
        for row in product_types:
            product_type_list.append(row)

        return product_type_list


    # Получение Названия, Стоимости, Фотографии товара по выбранной категории
    def get_products_by_cat(self, cat_code):
        name_price_photo = []
        query = self.session.query(
                self.product_table.columns.id,
                self.product_table.columns.product_name,
                self.product_table.columns.price,
                self.product_photos.columns.telegram_photo_id,
            ).filter(self.product_table.columns.product_photo_id == self.product_photos.columns.product_id). \
            filter(self.product_table.columns.product_type_id == f'{cat_code}')

        for row in query:
            name_price_photo.append(row)

        return name_price_photo


    # Добавление товара в корзину
    def add_to_cart(self, customer_id, product_id):
        query = self.session.execute(
                        self.cart.insert(),
                        {
                        'customer_id': f'{customer_id}',
                        'product_id': f'{product_id}',
                        },
                    )


    # Получение состава корзины по id пользователя
    def get_prod_details_from_cart(self, chat_id):
        product_names = self.session.query(
                        self.product_table.columns.product_name,
            ).filter(self.cart.columns.product_id == self.product_table.columns.id).filter(self.cart.columns.customer_id == f'{chat_id}')

        product_prices = self.session.query(
                        self.product_table.columns.price,
            ).filter(self.cart.columns.product_id == self.product_table.columns.id).filter(self.cart.columns.customer_id == f'{chat_id}')

        return product_names, product_prices


    # Очистка корзины пользователя
    def delete_users_cart(self, chat_id):
        self.session.query(self.cart).filter(self.cart.columns.customer_id == f'{chat_id}').delete(synchronize_session=False)
        self.session.commit()
