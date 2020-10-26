# Формирование корзины, подсчет количества товаров и общей стоимости
def generate_cart_innards(product_data):
    list_of_names = []
    list_of_prices = []
    for name_typle in product_data[0]:
        list_of_names.append(name_typle[0])
    for price_typle in product_data[1]:
        list_of_prices.append(price_typle[0])

    # После подсчета данные о количестве товаров добавляются в словарь,
    # за счет чего повторения названий уходят.
    product_dict = {}
    for item in list_of_names:
        quantity = list_of_names.count(item)
        product_dict.update({f'{item}':quantity})

    overal_price = sum(list_of_prices)

    return product_dict, overal_price
