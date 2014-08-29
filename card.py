# card.py
# Written by: Richard Walker
# Date: June 22, 2014

"""card.py
Provides a simple class for modeling a card
found in a standard playing deck"""

# Strings used to represent the ranks and suits of the cards.

ranks = ['Null','Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine',
         'Ten','Jack','Queen','King']

suits = {'d':'Diamonds',
         'c':'Clubs',
         'h':'Hearts',
         's':'Spades'}

class Card:

    """Provides a card object with the methods getRank(), getSuit(), BJValue()
    stripValue()."""

    def __init__(self, rank, suit):
        """Creates a card object with the given rank and suit.
        rank is an int in the range 1-13 indicating the ranks Ace-King,
        and suit is a single character 'd','c','h', or 's' indicating the suit."""

        self.rank = rank
        self.suit = suit

    def getRank(self):
        """Returns the rank of the card."""
        return self.rank

    def getSuit(self):
        """Returns the suit of the card."""
        return self.suit

    def BJValue(self):
        """Returns the black jack value of the card.
        Ace counts as 1, face cards count as 10"""
        if self.rank > 10:
            return 10
        else:
            return self.rank

    def stripValue(self):
        """Returns the Stripni value of the card.
        Ace counts as 4, Kings counts as 3, Queen counts as 2,
        Jack counts as 1, all else are 0"""
        if self.rank == 1:    #Ace
            return 4
        elif self.rank == 13: #King
            return 3
        elif self.rank == 12: #Queen
            return 2
        elif self.rank == 11: #Jack
            return 1
        else:
            return 0

    def __str__(self):
        return "%s of %s" % (ranks[self.rank],suits[self.suit])
   
