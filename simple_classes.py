
# instance = class()
# instance = class(args...)
colors = list()
print(colors)

letters = list('abcdef')
print(letters)

class Animal():
    def spam(self):
        print("spam spam spam spam")

a1 = Animal()
a2 = Animal()

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

d = Dog()
d.bark()
d.spam()

x = 5   #   x = int(5)
#   int x = 5;
#  String s = new String("Hello");


