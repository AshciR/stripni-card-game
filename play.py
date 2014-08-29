# play.py
# Written by: Richard Walker
# Date: June 25, 2014

"""play.py
Plays a game of Stripni between using a Text Interface."""

from stripni import Stripni
from textstripni import TextInterface

def main():
    """Initializes the text interface and Stripni application,
    then plays a game of Stripni."""

    print "----- HI, WELCOME TO THE STRIPNI GAME! -----\n"


    # Set the interface.   
    interface = TextInterface()

    # Make a Stripni game obeject.
    app = Stripni(interface)

    # Run the object.
    app.run()

    print ""
    raw_input("Press Enter to Exit...")

if __name__ == '__main__': main()
