from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Nelly")
d2 = CardDeck("Andy")

print(CardDeck)
print(d1, d2)

# CHEATER CHEATER CHEATER!!!
# print(d1._dealer)

print(d1.dealer)  # calls dealer.dealer()

d1.dealer = "Little Bear"  # __setattribute__()
print(d1.dealer)  # __getattribute__()

try:
    d1.dealer = 1234
except TypeError as err:
    print(err)
else:
    print(d1.dealer)  # property access
    print(d1.dealer.upper())

print(d1.get_dealer())  # function call
d1.set_dealer("Bonnie")

print(d1.cards, '\n')
d1.shuffle()
print(d1.cards, '\n')

for i in range(5):
    print("card:", d1.deal())
print()

print(d1.get_suits())
print(CardDeck.get_suits())
print('-' * 60)
j1 = JokerDeck("Jerry")
print(j1)
j1.shuffle()
print(j1.cards)
# print(len(d1.cards), len(j1.cards))
print(len(d1), len(j1))

