'''
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
'''


def end_zeros(number):
    index = -1
    count = 0
    number = str(number)

    for num in number:
        if number[index] != '0':
            break
        else:
            count += 1
            index -= 1

    return count



print(end_zeros(0))
print(end_zeros(1))
print(end_zeros(10))
print(end_zeros(101100))
