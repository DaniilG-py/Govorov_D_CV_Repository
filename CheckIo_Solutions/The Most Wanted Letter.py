def checkio(string):
    most_wanted_letter = []
    letter_dict = {}

    cleaned_string = string.replace(' ','').lower()

    for letter in cleaned_string:
        if letter.isalpha():
            letter_dict[letter] = cleaned_string.count(letter)

    max_value = max(letter_dict.values())

    for key in letter_dict:
        if letter_dict[key] == max_value:
            most_wanted_letter.append(key)

    most_wanted_letter = min(most_wanted_letter)

    return most_wanted_letter



print(checkio("Hello World!"))     # "l"
print(checkio("How do you do?"))   # "o"
print(checkio("One"))              # "e"
print(checkio("Oops!"))       # == "o"
print(checkio("AAaooo!!!!"))  # == "a"
print(checkio("abe"))         # == "a"
