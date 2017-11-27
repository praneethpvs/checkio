#!/usr/bin/env python
# Checking if the given password has length greater than 10.
# contains atleast a Digit, Upper case character, Lower case character.


def pwd_check(data):
    digit = False
    up_case = False
    low_case = False
    data = str(data)
    if len(data) >= 10:
        for char in data:
            if char.isdigit():
                digit = True
            if char.isupper():
                up_case = True
            if char.islower():
                low_case = True
        return True if digit and up_case and low_case else False
    else:
        return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert pwd_check('A1213pokl') == False, "1st example"
    assert pwd_check('bAse730onE4') == True, "2nd example"
    assert pwd_check('asasasasasasasaas') == False, "3rd example"
    assert pwd_check('QWERTYqwerty') == False, "4th example"
    assert pwd_check('123456123456') == False, "5th example"
    assert pwd_check('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete!")
