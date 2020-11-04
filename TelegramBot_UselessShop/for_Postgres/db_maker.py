import os
import sqlalchemy as sa



_USER_NAME = os.getenv('_USER_NAME')
_PASSWORD = os.getenv('_PASSWORD')
_HOST = os.getenv('_HOST')
_PORT = os.getenv('_PORT')
_BASE_NAME = os.getenv('_BASE_NAME')
_HEROKU_CLI = os.getenv('_HEROKU_CLI')


engine = sa.create_engine(f'postgresql://{_USER_NAME}:{_PASSWORD}@{_HOST}:{_PORT}/{_BASE_NAME}', echo=True)


conn = engine.connect()
metadata = sa.MetaData()

product_table = sa.Table(
                    'product_table',
                    metadata,
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('product_name', sa.String),
                    sa.Column('product_type_id', sa.Integer, sa.ForeignKey('product_types.id')),
                    sa.Column('price', sa.Integer),
                    sa.Column('product_photo_id', sa.Integer, sa.ForeignKey('product_photos.id')),
                )

product_photos = sa.Table(
                    'product_photos',
                    metadata,
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('product_id', sa.Integer, sa.ForeignKey('product_table.id')),
                    sa.Column('telegram_photo_id', sa.String),
                )

cart = sa.Table(
            'cart',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('customer_id', sa.Integer),
            sa.Column('product_id', sa.Integer, sa.ForeignKey('product_table.id')),
        )

product_types = sa.Table(
                    'product_types',
                    metadata,
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('product_type', sa.String),
                )

metadata.create_all(engine)


# Заполняем таблицы

types = (
        {'id':1, 'product_type':'Животные'},
        {'id':2, 'product_type':'Мебель'},
    )

product_items = (
            {'id':1, 'product_name':'Стол', 'product_type_id':2,'price': 540},
            {'id':2, 'product_name':'Кот', 'product_type_id':1,'price': 280},
            {'id':3, 'product_name':'Стул компьютерщика', 'product_type_id':2,'price': 15000},
            {'id':4, 'product_name':'Шкаф славянский', 'product_type_id':2,'price': 5400},
            {'id':5, 'product_name':'Собака', 'product_type_id':1,'price': 2980},
            {'id':6, 'product_name':'Попугай', 'product_type_id':1,'price': 18700},
            {'id':7, 'product_name':'Кровать', 'product_type_id':2,'price': 14650},
        )

product_item_photo = (
                {'product_photo_id':1},
                {'product_photo_id':2},
                {'product_photo_id':3},
                {'product_photo_id':4},
                {'product_photo_id':5},
                {'product_photo_id':6},
                {'product_photo_id':7},
            )

photos = (
        {
        'product_id':1,
        'telegram_photo_id':'AgACAgIAAxkBAAIBQV-HM3SrBdpMLJK7pCbguHKfvwtlAAI4sTEbvh45SFcJJDN0Lj9F4MXxly4AAwEAAwIAA20AA8OvAQABGwQ'
        },
        {
        'product_id':2,
        'telegram_photo_id':'AgACAgIAAxkBAAIBPV-HMw2da-LgE0MWbd8h4eW9-33mAAI0sTEbvh45SK2UhVjPeQZmHKJpli4AAwEAAwIAA20AA_OhAgABGwQ'
        },
        {
        'product_id':3,
        'telegram_photo_id':'AgACAgIAAxkBAAIBPl-HMyaY9ZEkT0w7KeNupyvhrm1PAAI1sTEbvh45SO6eRRMq2KZeZUzzly4AAwEAAwIAA20AA7-tAQABGwQ'
        },
        {
        'product_id':4,
        'telegram_photo_id':'AgACAgIAAxkBAAIBQl-HM4w46gqdY_bRpo3RewyB7dPgAAI5sTEbvh45SAUWGLtc7cRTLyjNly4AAwEAAwIAA20AA7ubAQABGwQ'
        },
        {
        'product_id':5,
        'telegram_photo_id':'AgACAgIAAxkBAAIBP1-HM0HgTXd83U79lFCDX1usRqgbAAI2sTEbvh45SNOp0LzYf5i72LRFmC4AAwEAAwIAA20AAx3CAQABGwQ'
        },
        {
        'product_id':6,
        'telegram_photo_id':'AgACAgIAAxkBAAIBQF-HM12vBvHYKCCuupFCoSrVCW1jAAI3sTEbvh45SO6KkxsKxGUPNrNFmC4AAwEAAwIAA20AA_PAAQABGwQ'
        },
        {
        'product_id':7,
        'telegram_photo_id':'AgACAgIAAxkBAAIBPF-HMtJtjjQPV0EtFvdss_rWzrQlAAIzsTEbvh45SC-n5UAIbxbTScnxly4AAwEAAwIAA20AA-KyAQABGwQ'
        },
    )


conn.execute(product_types.insert().values(types))
conn.execute(product_table.insert().values(product_items))
conn.execute(product_photos.insert().values(photos))

# Добавляем id фотографий в таблицу продуктов, так как таблица с внешними ключами создана
#
for i in range(len(product_items)):
    for photo_id in product_item_photo[i].values():
        conn.execute(product_table.update().where(product_table.c.id==f'{i+1}').values(product_photo_id = f'{int(photo_id)}'))


# Тестируем состав полученных таблиц

test = sa.select([product_table])
result = conn.execute(test)
print('table')
for row in result:
    print(row)

test = sa.select([product_types])
result = conn.execute(test)
print('types')
for row in result:
    print(row)

test = sa.select([product_photos])
result = conn.execute(test)
print('photo')
for row in result:
    print(row)

conn.close()
