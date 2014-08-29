# deck.py
# Written by: Richard Walker
# Date: June 23, 2014

"""deck.py
Provides a simple class for modeling a deck of cards
found in a standard playing deck."""

from card import Card
from random import randrange
import random

suits = ['d','c','h','s']


class Deck:

    """Represents a deck of cards."""

    def __init__(self,empty):
        """Creates a new empty deck or full deck of
        cards in a standard order."""
        # Create the empty deck.
        self.deck = []

        if not empty:
            # 2-D for loop to create the card objects.
            # The outer loop goes through each rank.
            # The inner loop goes through each suit.
            for rank in range(1,14):
                for suit in suits:
                    self.deck.append(Card(rank,suit))

    def cardsLeft(self):
        """Returns the number of cards reamining in the deck"""
        return len(self.deck)

    def shuffle(self):
        """Randomizes the order of the cards"""
        random.shuffle(self.deck)

    def listCards(self):
        """Prints the remaining cards in the deck"""
        for card in self.deck:
            print card

    def dealCard(self):
        """Returns a single card from the top of the deck and
        removes it from the deck"""

        try:
            # Pops a card from the top of the deck.
            # Top of the deck is the last element in the list.
            dealtCard = self.deck.pop()
            
            return dealtCard
        except IndexError:
            # The deck empty, return Nothing.
            print "The deck is empty." 
            return None

    def addCard(self,card):
        """Adds a given card object to the bottom of the deck"""
        self.deck.insert(0,card)

    def addCardTop(self,card):
        """Adds a given card object to the top of the deck"""
        self.deck.append(card)

    def addCardRand(self,card):
        """Adds a given card object randomly into the deck"""
        # (randrange - 1) picks a random position between
        # the 1st and last index exclusively. 
        self.deck.insert(randrange(1,(self.cardsLeft()-1)), card)

    def __str__(self):
        return "This is a deck containing %d cards." % (self.cardsLeft())
