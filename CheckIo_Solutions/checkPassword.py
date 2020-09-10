def checkio(password):
    pass_or_not = 0

    if len(password) < 10:
        return False

    for i in range(len(password)):
        if password[i].isdigit():
            pass_or_not += 1
            break
        else:
            continue

    for i in range(len(password)):
        if password[i].isupper():
            pass_or_not += 1
            break
        else:
            continue

    for i in range(len(password)):
        if password[i].islower():
            pass_or_not += 1
            break
        else:
            continue


    if pass_or_not == 3:
        return True
    else:
        return False

print(checkio('A1213pokl'))         # False
print(checkio('bAse730onE'))        # True
print(checkio('asasasasasasasaas')) # False
print(checkio('QWERTYqwerty'))      # False
print(checkio('123456123456'))      # False
print(checkio('QwErTy911poqqqq'))   # True
