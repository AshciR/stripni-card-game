# player.py
# Written by: Richard Walker
# Date: June 23, 2014

"""player.py
Provides a class for modeling a player of a card game"""

from deck import Deck

class Player:
    """Represents a Player."""

    # Holds the number of player instances created.
    numPlayers = 0

    def __init__(self,name):
        """Creates a new player with the given name and an empty deck.
        The player's turn is false by default"""
        self.name = name

        # Increase the number of player's created
        Player.numPlayers += 1

        # Sets player's turn to false by default
        self.turn = False

        # Create the empty deck.
        self.deck = Deck(True) 

    @staticmethod
    def getNoPlayers():
        """Returns the number of players created"""
        return Player.numPlayers

    def getName(self):
        """Returns the player's name"""
        return self.name

    def getTurn(self):
        """Returns the player's turn"""
        return self.turn

    def toggleTurn(self):
        """Changes the player turn from whatever
        boolean value it currently has"""
        self.turn = not self.turn

    # Player's Deck Methods -----------------------------------
    
    def addCard(self,card):
        """Adds a given card object to the bottom of the deck"""
        self.deck.addCard(card)

    def cardsLeft(self):
        """Returns the number of cards reamining in the deck"""
        return self.deck.cardsLeft()

    def shuffle(self):
        """Randomizes the order of the cards"""
        self.deck.shuffle()

    def listCards(self):
        """Prints the remaining cards in the deck"""
        self.deck.listCards()

    def dealCard(self):
        """Returns a single card from the top of the deck and
        removes it from the deck"""
        return self.deck.dealCard()

    def __str__(self):
        return "This is a player whos name is %s." % (self.getName())
   
