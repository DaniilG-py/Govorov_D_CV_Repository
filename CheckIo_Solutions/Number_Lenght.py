'''
You have a positive integer. Try to find out how many digits it has?

Input: A positive Int

Output: An Int.

Example:

number_length(10) == 2
number_length(0) == 1
'''


def number_length(number):
    return len(str(number))


print(number_length(10))
