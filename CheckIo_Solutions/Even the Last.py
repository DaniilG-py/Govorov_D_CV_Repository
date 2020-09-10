'''
You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.
'''


def checkio(list_of_nums):

    if len(list_of_nums) == 0:
        answer = 0
    else:
        sum_of_evens = sum(list_of_nums[0::2])
        answer = sum_of_evens * list_of_nums[-1]

    return answer




print(checkio([0, 1, 2, 3, 4, 5])) # == 30
print(checkio([1, 3, 5])) # == 30
print(checkio([6])) # == 36
print(checkio([])) # == 0
