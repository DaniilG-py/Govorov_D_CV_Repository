'''
You should return a given string in reverse order.

Input: A string.

Output: A string.

Example:

backward_string('val') == 'lav'
backward_string('') == ''
backward_string('ohho') == 'ohho'
backward_string('123456789') == '987654321'
'''


def backward_string(string):
    return string[::-1]

print(backward_string(''))
