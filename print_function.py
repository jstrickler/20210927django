
a = 124
b = 15.23920938
c = "rhubarb"

sep = ' '
end = '\n'
print(a, b, c)
print(str(a) + sep + str(b) + sep + str(c))
print('foo')  # adds \n
print('bar')

print(a, b, c, sep="/")
print(a, b, c, sep=", ")
print(a, b, c, sep='')

print('foo', end=' ')
print('bar')
print('foo', end='')
print('bar')

toon = "Fred Flintstone"
city = "Bedrock"
print(toon, "lives in", city)
print("{:25s} {:25s}".format(toon, city))

toon = "Yogi Bear"
city = "Jellystone Park"
print("{:25s} {:25s}".format(toon, city))

print(b)
print("{:.2f}".format(b))   # printf("%s %d %f\", a, b, c);

print("{} lives in {}".format(toon, city))
print(f"{toon} lives in {city}")
print(f"Value is {b:.2f}")









