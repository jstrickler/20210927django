
FILE_NAME = 'DATA/mary.txt'

mary_in = open(FILE_NAME, 'r')
# read data here...
mary_in.close()

with open(FILE_NAME) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove trailing whitespace
        print(line)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()
    print("raw:")
    print(repr(contents), '\n')
    print("normal:")
    print(contents)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)


with open('DATA/alice.txt') as alice_in:
    with open('rabbit.txt', 'w') as rabbit_out:
        for raw_line in alice_in:
            if 'rabbit' in raw_line.lower():
                rabbit_out.write(raw_line)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
            fruits_out.write("%s\n" % (fruit.upper()))



