# build a card class as specified on Udemy 'Modern Python3 Bootcamp' Lec 25:
from random import shuffle


class Card:

    valid_suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    valid_values = ('A', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, value, suit) -> None:
        if type(suit) != str or type(value) != str:
            raise TypeError('suit and value must be strings')
        elif suit not in Card.valid_suits:
            raise ValueError('Not a valid suit')
        elif value not in Card.valid_values:
            raise ValueError('Not a valid card value')
        else:
            self.suit = suit
            self.value = value

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"


# if __name__ == "__main__":
#     # my_card = Card('k', 30)
#     my_card = Card('Spades', 'A')
#     print(my_card)

class Deck:

    def __init__(self):
        suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        values = ('A', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K')
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min(count, num)
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)
print(d.count())
