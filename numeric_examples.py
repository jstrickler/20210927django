
i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100  # not 0100

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.3234e31

a = 19
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # "true" division
print(a // b)  # floored division -- round down to whole #
print(a ** b)  # power
print(a ** .5)  # square root
print(a % b)  # remainder AKA modulo

x = 10
x += 5  # x = x + 5
x *= 6
x /= 2
print(x)
print()

#  NO!!   x++ ++x x-- --x

a = "123"
b = 456
print(a + str(b))
print(int(a) + b)

# str(anything)
# int(number or string)   (string must look like int)
# float(number or string)  (string must look like float)
# bool(anything)

# list(iterable)
# dict(iterable-of-pairs)
# dict(name=value, ...)
# set(iterable)

