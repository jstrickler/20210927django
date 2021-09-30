#!/usr/bin/python3

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

# def cleanup()....

for s in spam:
    new_s = cleanup(s)
    print("OLD:", s)
    print("NEW:", new_s)
    print()
