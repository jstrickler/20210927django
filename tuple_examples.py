

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

person2 = 'Bill', 'Gates', 'Microsoft', '1955-10-28', ('123 Rich Guy Lane', 'Mercer', 'WA')


#  see namedtuple in the collections module

print(person)
print(person[0])
print(person[0], person[1])

first_name, last_name, product, dob = person  # unpack iterable

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]
print(type(people))
print(people[0], type(people[0]))
print(people[0][0])
print(people[0][0][0])
print()

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, dob, product)
print()


values = [1, 2, 3, 4, 5, 6, 7, 8]

a, b, *c = values
print(a, b, c)
a, *b, c = values
print(a, b, c)
*a, b, c = values
print(a, b, c)








