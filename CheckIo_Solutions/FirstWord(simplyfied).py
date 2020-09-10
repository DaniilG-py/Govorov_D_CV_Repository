'''
Дана строка и нужно найти ее первое слово.

Это упрощенная версия миссии First Word.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
Входные параметры: Строка.

Выходные параметры: Строка.

Пример:

first_word("Hello world") == "Hello"
'''


def first_word(string):
    splited_str = string.split(' ')
    return splited_str[0]


print(first_word('Hello World'))    
