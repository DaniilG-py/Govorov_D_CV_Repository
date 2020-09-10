'''
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.

Output: The market identifier code (ticker symbol) as a string.
'''


def best_stock(dictionary):

    for key, value in dictionary.items():
        if value == max(dictionary.values()):
            return key



print(best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
})) #== 'ATX'


print(best_stock({
    'CAC': 91.1,
    'ATX': 1.01,
    'TASI': 120.9
})) #== 'TASI'
