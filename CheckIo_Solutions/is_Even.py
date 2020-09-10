'''
Check is the given number is even or not. Your function shoudl return True if the number is even, andFalse if the number is odd.

Input: Int.

Output: Bool.
'''


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False






print(is_even(2))# == True
print(is_even(5))# == False
print(is_even(0))# == True
