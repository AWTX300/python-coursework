from random import *

heart = "\u2665"
diamond = "\u2666"
spade = "\u2660"
club = "\u2663"

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = [heart, diamond, spade, club]
cards = [''.join([v, s]) for s in suits for v in values]

print(cards, '\n')
shuffle(cards)
print(cards, '\n')

print(cards.pop(), '\n')
print(cards)
