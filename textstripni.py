# textstripni.py
# Written by: Richard Walker
# Date: June 23, 2014

"""textstripni.py
Provides a text-based interface for the Stripni game."""

from card import Card

class TextInterface:

    """Creates a text-based interface for the Stripni game"""

    def __init__(self):
        """Creates a new player with the given name and an empty deck.
        The player's turn is false by default"""

        print "Let's play some Stripni!\n"

    def getPlayerName(self,num):
        """Asks the user for a player's name. Returns the given name"""
        ans = raw_input("What is Player %d's name? " % num)  
        return ans

    def automate(self):
        """Ask if the user wants to automate the game or not."""
        print "\nDo you want to automate the game?"
        ans = raw_input("Type 'Yes' if you do. Any other answers will be a 'No': ")  
        return ans[0] in "yY"

    def getWaitTime(self):
        """Asks the user for the wait time inbetween card draws (in seconds).
        Returns the wait time casted as a float if it's between 0 and 5 seconds (inclusive).
        Returns False otherwise"""
        
        ans = raw_input("\nHow long do you want to wait between card draws? (Max Time is 5 seconds): ")
                        
        try:
            ans = float(ans)
            # Check if the ans is between 0 and 5 seconds (inclusive).
            if (ans > 0 and ans <= 5):
                return ans
            else:
                print "The number is not between 0 and 5 seconds.\n"
                return False
        # Catches non-numeric answers.
        except ValueError:
            print "That's not a number.\n"
            return False

    def startMsg(self):
        """Annoucnes that the game is starting""" 
        print "" # Blank line
        print "---------------------"
        print "LET'S START THE GAME!"
        print "---------------------"
        print "" # Blank line

    def shuffle(self):
        """Annoucnes that the deck is being shuffled""" 
        print "\nShuffling the deck..."

    def splitDeck(self):
        """Annoucnes that the deck is being split""" 
        print "\nSplitting the deck..."

    def dealCards(self, name):
        """Takes the player's name, and announces that he/she is dealing
        from their deck.""" 
        print "Dealing from %s's deck." % (name)
    
    def announceTurn(self, name):
        """Announces who's turn it is."""
        print "It's %s's turn." % (name)

    def announceCard(self, card):
        """Announces what card was played."""
        print card.__str__() + " was played.\n"

    def valueCard(self,value,player):
        """Announces that a value card was played."""
        print "A value card was played!"
        print "If the next player doesn't find a value card"
        if (value == 1):
            print "in the next draw, then %s will win this round." % (player)
        else:
            print "in the next %d draws, then %s will win this round." % (value,player)
        print "\nSwitching to the next player.\n"

    def announceTurnWinner(self, name):
        """Announces who won that turn"""
        print "%s won that round!\n" % (name)

    def dealWinner(self, name):
        """Announces that it is dealing the main deck into the winner's deck."""
        print "Adding the main deck to the bottom of %s's deck...\n" % (name)

    def closeMsg(self,winner,loser):
        """Announces the winner and loser of the game."""
        print "\n%s won the game!" % (winner.getName())
        print "Sorry %s, better luck next time." % (loser.getName())
        print ""
        print "Thanks for playing!"


