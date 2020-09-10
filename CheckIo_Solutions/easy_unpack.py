def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return (elements[0], elements[2], elements[-2])


print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))) #== (1, 3, 7)
print(easy_unpack((1, 1, 1, 1))) #== (1, 1, 1)
print(easy_unpack((6, 3, 7))) #== (6, 7, 3)
