'''
Найдите ближайшее значение к переданному.

Вам даны список значений в виде
множества (Set) и значение, относительно которого, надо найти ближайшее.

Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.

Несколько уточнений:

Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
Ряд чисел всегда не пустой, т.е. размер >= 1;
Переданное значение может быть в этом ряде, а значит оно и является ответом;
В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
Ряд не отсортирован и состоит из уникальных чисел.
Input: Два аргумента. Ряд значений в виде set. Искомое значение - int

Output: Int.
'''

def nearest_value(set_of_nums, number):
    set_of_nums = set(set_of_nums)
    if len(set_of_nums) == 1:
        return list(set_of_nums)[0]
    for num in set_of_nums:
        if num == number:
            return number

    set_of_nums.add(number)
    set_of_nums = sorted(set_of_nums)
    number_index = set_of_nums.index(number)

    if number_index == 0:
        return set_of_nums[1]
    elif number_index == len(set_of_nums)-1:
        return set_of_nums[-2]
    else:
        nearest_list = [set_of_nums[number_index-1], number, set_of_nums[number_index+1]]

    if nearest_list[2] - number == number - nearest_list[0]:
        # print('1')
        return min(nearest_list)
    elif nearest_list[2] - number > number - nearest_list[0]:
        # print('2')
        return nearest_list[0]
    elif nearest_list[2] - number < number - nearest_list[0]:
        # print('3')
        return nearest_list[2]

# def nearest_value(values: set, one: int) -> int:
#     L_values = sorted(list(values))
#     diff = [abs(v - one) for v in L_values]
#     return L_values[diff.index(min(diff))]


print(nearest_value([400,748,106,118,172,197], 18))
print(nearest_value({2, 9, 8}, 9))
print(nearest_value({3, 7, 10, 11, 12, 17}, 5)) # == 3
print(nearest_value({4, 7, 10, 11, 12, 17}, 9))# == 10
print(nearest_value({4, 7, 10, 11, 12, 17}, 8))# == 7
