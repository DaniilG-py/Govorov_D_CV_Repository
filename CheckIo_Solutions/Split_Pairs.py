'''
Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').

Входные данные: Строка.

Входные данные: An iterable of strings.
'''

def split_pairs(str_of_smth):
    if len(str_of_smth) % 2 != 0:
        str_of_smth = str_of_smth + '_'

    answer = [str_of_smth[i:i+2] for i in range(0, len(str_of_smth), 2)]

    return answer


print(split_pairs('abcd'))# == ['ab', 'cd']
print(split_pairs('abc'))# == ['ab', 'c_']
