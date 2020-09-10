'''
Not all of the elements are important. What you need to do here is to remove from the list all of the elements before the given one.

example

For the illustration we have a list [3, 4, 5] and we need to remove all elements that go before 3 - which is 1 and 2.

We have two edge cases here: (1) if a cutting element cannot be found, then the list shoudn't be changed. (2) if the list is empty, then it should remain empty.

Input: List and the border element.

Output: Iterable (tuple, list, iterator ...).

Example:

remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
'''


def remove_all_before(list_of_nums, border):
    if len(list_of_nums) == 0:
        return list_of_nums

    for elem in list_of_nums:
        if border in list_of_nums:
            return list_of_nums[list_of_nums.index(border):]
        else:
            return list_of_nums






print(remove_all_before([1, 2, 7, 4, 5], 3))
print(remove_all_before([], 3))
