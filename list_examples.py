list1 = list()   # new, empty list
a = 10
b = 15
list2 = [1, 2, 3, 4, a, b]  # literal list
list3 = []  # empty list

cities = ["Toronto", "New York", "Houston", "Palo Alto",
          "Durham", "Cary", "Dallas"]

print(cities)
cities.append("Ottawa")
print(cities)
cities.append("Calgary")
print(cities)

cities.insert(0, "San Antonio")
cities.insert(4, "Montreal")
print(cities)

more_cities = ['Pittsburgh', 'Austin', 'Mountain View']

cities.extend(more_cities)
print(cities)

#  LIST.append(obj)  LIST.insert(pos, obj)
#  LIST.extend(iterable)

print(cities[0], cities[5])
del cities[5]   # del cities

c = cities.pop()
print(c)
print(cities)
print()
c = cities.pop()
print(c, cities)
print()

c = cities.pop(2)   # remove by postion (and return)
print(c, cities, '\n')

cities.remove('Durham')  # remove by value
print(cities)

#  del LIST[pos]    value = LIST.pop(pos=0)
#  LIST.remove(value)

all_food = ['spam', 'spam', 'spam', 'spam', 'spam',
            'spam', 'spam', 'spam', 'spam',
            'spam', 'spam', 'spam', 'eggs', 'spam']

print(all_food.count('spam'), all_food.count('eggs'),
      all_food.count('toast'))

print(all_food.index('eggs'))
print(all_food.index('spam'))
item = 'toast'
if item in all_food:
    print(all_food.index(item))

print(cities)
print(cities[0], cities[4], cities[-1], cities[len(cities)-1])

#  [start:stop]  [:stop]   [start:]  [start:stop:step]

print(cities[0:4])
print(cities[:4])
print(cities[2:6])
print(cities[5:])
print(cities[-3:])
print(cities[::1])
print(cities[::])
print(cities[::2])
print(cities[::3])

text = 'xh2e@lrlyo'
print(text[1::2], '\n')

for city in cities:
    print(city)
print()

# for VAR in ITERABLE:
#     ...

s = "abcde"
for letter in s:
    print(letter)
print()

for direction in "north south east west".split():
    print(direction)
print()

for d in "n", "s", "e", "w":
    print(d)
print()











