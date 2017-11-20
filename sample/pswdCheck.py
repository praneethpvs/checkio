#!/usr/bin/env python
# Python function to check if a given password has length > 5, has a Digit and an Uppercase letter.


def func(text):
    digit = False
    caps = False
    text = str(text)
    if len(text) > 5:
        for char in text:
            if char.isdigit():
                digit = True
            if char.isupper():
                caps = True
        if digit and caps:
            print("Good Password")
        else:
            print("Password needs a Digit and an Uppercase letter")
    else:
        print("Password length should be greater than 5")

func("pswd")
