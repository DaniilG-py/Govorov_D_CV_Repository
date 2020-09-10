'''
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.
'''

def beginning_zeros(number):
    count_zero = 0

    if number.startswith('0'):

        for num in number:
            if num == '0':
                count_zero += 1
            else:
                break
        return count_zero
    else:
        return count_zero






print(beginning_zeros('100'))# == 0
print(beginning_zeros('001'))# == 2
print(beginning_zeros('100100'))# == 0
print(beginning_zeros('001001'))# == 2
print(beginning_zeros('012345679'))# == 1
print(beginning_zeros('0000'))# == 4
