import random
print("Hello World")

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print(f"{self.value} of {self.suit}")

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
class Player(object):
    def __init__(self):
        pass

card = Card("clubs", 3)
deck = Deck()
deck.shuffle()