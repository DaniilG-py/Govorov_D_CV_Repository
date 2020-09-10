def checkio(passw):
    digits = [dig for dig in passw if dig.isdigit()]
    uppers = [upp for upp in passw if upp.isupper()]
    lowers = [low for low in passw if low.islower()]
    return True if len(digits) and len(uppers) and len(lowers) and (len(passw) >= 10) else False



    #These "asserts" using only for self-checking and not necessary for auto-testing
print(checkio('A1213pokl'))         # False
print(checkio('bAse730onE'))        # True
print(checkio('asasasasasasasaas')) # False
print(checkio('QWERTYqwerty'))      # False
print(checkio('123456123456'))      # False
print(checkio('QwErTy911poqqqq'))   # True
