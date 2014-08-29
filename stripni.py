# stripni.py
# Written by: Richard Walker
# Date: June 23, 2014

"""stripni.py
Plays a game of stripni."""

from deck import Deck
from player import Player

import time

class Stripni:

    """Represents a game of Stripni."""

    def __init__(self,interface):
        """Creates a new stripni game with the given interface.
        Also creates a deck with the 52 standard playing cards."""
        self.interface = interface

        # Make the standard card deck
        self.deck = Deck(False)

    def run(self):
        """Runs the Stripni Game"""
        # Ininitalizing the game
        self.createPlayers()
        self.splitCards()

        # Starting the game message
        self.interface.startMsg()
        
        # Player one goes first by default
        self.player1.toggleTurn()
        self.interface.announceTurn(self.player1.getName())

        # Sets current player to player 1, because we toggled it on
        # above.
        currentPlayer = self.whooseTurn()
        result = self.playTurn(currentPlayer)

        # The game finishes when either player's deck is finished,
        # So keep playing rounds until this happens.
        
        while (True):
            # Player ran out of cards, finish the game.
            if(result == None):
                break
            # If the value was 0, then it's the next player's turn
            elif(result == 0):
                self.togglePlayers()
                currentPlayer = self.whooseTurn()
                self.interface.announceTurn(currentPlayer.getName())
                
                result = self.playTurn(currentPlayer)
            # A value card was played, keep drawing until the player
            # gets a value card, draws the value amount,
            # or is out of cards.
            else:
                self.interface.valueCard(result,currentPlayer.getName())
                self.togglePlayers()
                currentPlayer = self.whooseTurn()
                self.interface.announceTurn(currentPlayer.getName())

                result = self.playValue(currentPlayer, result)

                # The player lost the round, and the main
                # deck goes to the other player.
                if (result == 0):
                    self.drawMainDeck()

        # Store winnner and loser
        loser = currentPlayer
        self.togglePlayers()
        winner = self.whooseTurn()

        # The game is finished, clean up.
        self.finishGame(winner,loser)

    def finishGame(self,winner,loser):
        """Outputs the result of the game to the user"""
        self.interface.closeMsg(winner,loser)

    def drawMainDeck(self):
        """Places all the cards in the main deck into the winners' deck"""
        # Temporarily toggle to the winner
        self.togglePlayers()
        # Determine the winning player
        winner = self.whooseTurn()
        self.interface.announceTurnWinner(winner.getName())
        
        self.interface.dealWinner(winner.getName())

        # Simulate time spent adding cards to the bottom
        # if the game isn't in automated mode
        if (not self.automate):
            time.sleep(0.5) 

        while (self.deck.cardsLeft() != 0):
            # Deals from main deck into winning player deck
            dealtCard = self.deck.dealCard()
            winner.addCard(dealtCard)

        # Toggle back to the loser of the last round
        self.togglePlayers()

    def playValue(self, player, maxDraws):
        """Runs a player's turn until a value card is played"""
        # Tracks how many cards have been drawn
        # by the player during this turn.
        drawCount = 0

        # The player keeps dealing cards until deck is finished
        # or until a value card is dealt. 
        while(drawCount < maxDraws):
            # Wait the given time before next deal
            self.dealTimer(self.automate)

            # Deal the card top card from the player's deck
            dealtCard = player.dealCard()

            # The player's deck is empty, they lost.
            if(dealtCard == None):
                return None
            else:
                self.interface.announceCard(dealtCard)
                # Add the dealt card to the main deck
                self.deck.addCard(dealtCard)
                # Increment drawCount
                drawCount += 1

            # If the player dealt a value card, return that value.
            if( dealtCard.stripValue() > 0 ):
                # Break the while loop
                break

        # Which would be 0
        return dealtCard.stripValue()

    def dealTimer(self,option):
        """Determines is the game should be automated or
        wait on user input"""
        # User choose to automate the game
        if (option):
            time.sleep(self.wait)
        else:
            raw_input("Press Enter to draw the next card.\n")
            time.sleep(0.25) # Pause a few secs to simulate drawing
    
    def playTurn(self,player):
        """Plays the given player's turn.
        If the player's deck is empty, then None is returned.
        Else card's value is returned."""

        # Wait the given time before next deal
        self.dealTimer(self.automate)

        # Deal the card top card from the player's deck
        dealtCard = player.dealCard()

        # The player's deck is empty, they lost.
        if(dealtCard == None):
            return None
        else:
            # Announce the card
            self.interface.announceCard(dealtCard)
            # Add the dealt card to the main deck
            self.deck.addCard(dealtCard)
            # Return the card's value
            return dealtCard.stripValue()

    def togglePlayers(self):
        """Toggles the players' turns"""
        # If player 1 is on, turn him/her off 
        # and turn player 2 on
        if(self.player1.getTurn()):
            self.player1.toggleTurn()
            self.player2.toggleTurn()
        # Else it means player 2 is on,
        # so do accordingly.
        else:
            self.player2.toggleTurn()
            self.player1.toggleTurn()
                
    def createPlayers(self):
        """Gets the information for player 1 and player 2 and creates them.
        Also get the time to wait inbetween draws"""
        # Create Player One
        playerOne = self.interface.getPlayerName(Player.getNoPlayers() + 1)
        self.player1 = Player(playerOne)

        # Create Player Two
        playerTwo = self.interface.getPlayerName(Player.getNoPlayers() + 1)        
        self.player2 = Player(playerTwo)

        # Ask if the user wants to automate the game or not
        self.automate = self.interface.automate()

        # The user wants it to be automated
        if self.automate:
            # Determine the wait time between card draws
            while True:
                self.wait = self.interface.getWaitTime()
                # if self.wait is not an appropiate value
                # it returns a False.
                if (not(not self.wait)):
                    break 
            

    def splitCards(self):
        """Shuffles and splits the cards between the players"""
        # Shuffle the cards
        self.interface.shuffle()
        time.sleep(1.5) # Wait a few secs while shuffling
        self.deck.shuffle()

        # Split the cards evenly between the players
        self.interface.splitDeck()
        time.sleep(1.5) # Wait a few secs while splitting
        while (self.deck.cardsLeft() != 0):
            # Deals from main deck into player one's deck
            dealtCard = self.deck.dealCard()
            self.player1.addCard(dealtCard)

            # Deals from main deck into player two's deck
            dealtCard = self.deck.dealCard()
            self.player2.addCard(dealtCard)
   
    
    def whooseTurn(self):
        """ Determines which player's turn it is"""
        if self.player1.getTurn():
            return self.player1
        else:
            return self.player2
    
    def __str__(self):
        return "This is a game of stripni using the %s interface." % (self.interface)
