colors1 = 'red green red red blue purple yellow black pink'.split()
colors2 = 'pink red blue mauve green blue blue blue white black'.split()
print(colors1)
print(colors2)
print()

c1 = set(colors1)
c2 = set(colors2)
c1.add('brown')
c2.add('cerise')
print(c1)
print(c2)
print()
print("common:", c1 & c2)   # intersection
print("NOT common:", c1 ^ c2)  # xor
print("all:", c1 | c2)  # union
print("just c1:", c1 - c2)
print("just c2:", c2 - c1)

names = {'Andy', 'Little Bear', 'Nelly', 'Bonnie'}

for i in range(1000):
    c1.add('purple')
print(c1)
