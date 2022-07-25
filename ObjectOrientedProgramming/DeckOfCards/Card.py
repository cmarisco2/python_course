# build a card class as specified on Udemy 'Modern Python3 Bootcamp' Lec 25:

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


if __name__ == "__main__":
    # my_card = Card('k', 30)
    my_card = Card('Spades', 'A')
    print(my_card)
