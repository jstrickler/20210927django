import os

def get_message():
    return "Hello Python world!"

m = get_message()
print(m)
print(get_message())

def show_message():
    message = get_message()
    print("Message is:", message)

show_message()

def animal(animal_type, animal_name):
    print("I have a(n) {} -- its name is {}".format(animal_type, animal_name))

animal('English shepherd', 'Nellie')
animal('Python', 'Pauline')
print()

def hello(whom="world"):
    print("Hello,", whom)

hello("New York!")
hello("Dolly")
hello()
print()


def find_term(term, *file_names):
    """
    Print all lines of specified files which contain specified string.

    :param term: search term
    :param file_names: one or more file paths
    :return: None
    """
    for file_name in file_names:
        short_name = os.path.basename(file_name)
        with open(file_name) as file_in:
            for line in file_in:
                if term in line:
                    print("{}: {}".format(short_name, line.rstrip()))

find_term('chicken', 'DATA/parrot.txt')
print()
find_term('Lizard', 'DATA/alice.txt')
print()
find_term('bird', 'DATA/alice.txt', 'DATA/parrot.txt')
print()
find_term('wombat')
print()

def locate(*, latitude, longitude):
    pass

locate(latitude=123.4, longitude=37.9)
locate(longitude=19.32, latitude=58.9)

def config(**values):
    print("values:", values)

config(filename="wombats.txt", username="Mathilda", country="Burkina Faso")

def universal(*args, **kwargs):
    pass

#         pos          named
#         req req opt  req req opt
def wacky(p1, p2, *p3, p4, p5, **p6):
    pass

wacky('a', 'b', p4='c', p5='d')
wacky('a', 'b', p5='d', p4='c')
wacky('b', 'a', p4='c', p5='d')

wacky('a', 'b', 'i', 'j', 'k', 'l', p4='c', p5='d')

wacky('a', 'b', 'i', 'j', 'k', 'l', p4='c', p5='d', foo="mango",
      bar="terrapin", food="snozzcumber")





























