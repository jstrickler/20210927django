
x = 100  # global var


def spam():
    x = "factor"  # STILL local var
    y = 50  # local var
    print("in spam(): x is", x)


spam()
print("in main: x is", x)

#
