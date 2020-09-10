"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.
"""
def checkio(number):
    number = str(number).replace('0', '')

    num = 1
    for x in number:
        num *= int(x)
    return num



print(checkio(123405))    # == 120
print(checkio(999))       # == 729
print(checkio(1000))      # == 1
print(checkio(1111))      # == 1
