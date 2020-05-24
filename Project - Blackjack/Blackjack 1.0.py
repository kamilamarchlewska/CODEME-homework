class Card:

    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['♣', '♦', '♥', '♠']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand:

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + ' '
        else:
            rep = '<empty>'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)

# main part
card1 = Card(rank='A', suit='c')

print('I display a card object ( class Card ):')
print(card1)
card2 = Card(rank='2', suit='c')
card3 = Card(rank='3', suit='c')
card4 = Card(rank='4', suit='c')
card5 = Card(rank='5', suit='c')

print('\nI display the rest of the objects - one by one object:')
print(card2)
print(card3)
print(card4)
print(card5)


myHand = Hand()
myHand.add(card1)
myHand.add(card2)
myHand.add(card3)
myHand.add(card4)
myHand.add(card5)
print('\nI display the content of my hand - after adding 5 cards:')
print(myHand)

yourHand = Hand()
myHand.give(card1, yourHand)
myHand.give(card2, yourHand)
print('\nGives 2 cards to your hand.')
print("----------------------------------")
print('Your hand:')
print(yourHand)
print('My hand:')
print(myHand)

myHand.clear()
print('\nMy hand after removing the cards:')
print(myHand)
input('\n\nTo end the program press enter.')