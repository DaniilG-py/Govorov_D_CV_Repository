'''
In a given list the first element should become the last one.
An empty list or list with only one element should stay the same.
'''


def replace_first(list_of_nums):
    if list_of_nums:
        list_of_nums.append(list_of_nums.pop(0))
        return list_of_nums
    else:
        return list_of_nums



print(replace_first([1, 2, 3, 4]))# == [2, 3, 4, 1]
print(replace_first([]))# == [1]
