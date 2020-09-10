'''
You are the beginning of a password series. Every mission will be based on the previous one. Going forward the missions will become slightly more complex.

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6.
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == True
'''


def is_acceptable_password(password):
    if len(password) > 6:
        return True
    else:
        return False


print(is_acceptable_password('short'))
print(is_acceptable_password('muchlonger'))
