# Justin Thomas MIT211573
# 20th October 2021
# MN404 Fundamentals of Operating Systems and Programming
# Assignment 2 
# This program plays a Game of Nim with two human players and one AI player
# It randomly selects whether human player 1 or 2 has the first turn.
# 
# It validates user input including a user:
#    - entering a number out of bounds
#    - entering a null value
#    - entering a string value to an input requiring an integer
#
# Variables:
#   stones is the number of stones in the pile
#   playagain is whether the player wishes to play the game again
#   player1.name is human player 1 name in title case
#   player2.name is human player 2 name in title case
#   player1.mitid is human player 1 student id in title case
#   player2.mitid is human player 2 student id in title case
#   player is who the current player is 0 (computer), 1 or 2
#   stonesremoved is the number of stones removed by a player
#   check is used to set a condition to validate input
#   curplayer.name is the name of the current human player
#   curplayer.mitid is the student number of the current human player
#
# Import the random library so we can use it to choose a random number
import random

# Define a class for the human players
class Players():
    
    # To create the instance  
    def __init__(self,name,mitid):
            # Set instance attributs
            self.name = name
            self.mitid = mitid
            
# Define a class for the current human player
class CurrentPlayer():

    # To create the instance  
    def __init__(self,name,mitid):
            # Set instance attributes
            self.name = name
            self.mitid = mitid
 
# I've used a function here for the game introduction
# including using a multi-line print.
def intro():
 print("")
 print("--------------------------------------")
 print("This is the game of NIM. I am the AI player.")
 print("Each player in turn chooses a number of stones to remove from the pile."
 " The number removed must be between 1 and 3 stones."
 " If you enter text instead a random number of stones will be chosen for you."
 " The last player to remove stones wins!")
 
# Define a function to check if the user hasn't entered anything in text input
def checknullinput(x):
   # I need global varibles so the values are set outside the function
   global check
   # If the user hasn't entered anything
   if x == "":
      # Show an error 
      print("Error: you haven't entered anything.")
      check = True
   else:
      # Otherwise the check condition is ok and set to false 
      check = False

# Define a function to check if player has removed no stones and remove 
# a random number of stones between 1 and 3 inclusive if so
def randomstones():
    # I need global varibles so the values are set outside the function
    global check
    global stonesremoved

    stonesremoved = int(random.choice([1,3]))
    print(f"Invalid input so a random {stonesremoved} stones removed")
    check = False

def main():
 # Set the initial number of stones
 stones = 0
 # Set the initial number of stones to remove
 stonesremoved = 0
 # Set player
 player = 0
 # Set the initial play state to playing
 playagain = "y"    
 # Create the players, we will populate the attributes when entered by the user
 player1 = Players("","")
 player2 = Players("","")
 curplayer = CurrentPlayer("","")      
 # Run the function to display the intro
 intro()
 # Set an initial state for the input checks
 check = True
 # Ask for the player names and store them in title case   
 while check == True:
  # Inputs in Python default to string, but I think it is a good idea
  # to specific  
  player1.name = str(input("Enter the name of player 1: ").title())
  # use the function to check the user entered something
  checknullinput(player1.name)
  # Reset the check flag for the next check
 check = True
 while check:
   player1.mitid = str(input("Enter the MITID of player 1: ").title())
   checknullinput(player1.mitid)
 check = True
 while check:   
    player2.name = str(input("Enter the name of player 2: ").title())
    checknullinput(player2.name)
 check = True
 while check:     
    player2.mitid = str(input("Enter the MITID of player 2: ").title())
    checknullinput(player2.mitid)
 check = True
 # ======================================================================
 # This is the main loop of the game
 # It starts here so the players don't have to enter their details
 # in again if they choose to play another game.
 # While the playagain state is y continue to play
 # ======================================================================
 while playagain == "y":
    print("")
    print(f"Welcome {player1.name} and {player1.name}.")
    # Use randomisation to pick which human player will get the first turn
    # player = random.choice([1,2])
    player = random.choice([1,2])
    # Set the identity of the current player. I use these to display the
    # current player details while playing and if they win
    if player == 1:
        curplayer.name = player1.name
        curplayer.mitid = player2.mitid
    elif player == 2:
        curplayer.name = player2.name
        curplayer.mitid = player2.mitid
    # Just a blank line
    print("")
    # Tell the player who goes first
    print(f"{curplayer.name} will have the first turn and pick the number of starting stones.")
    # Loop the request until a number of stones between 30 and 50 is entered
    # and catch invalid input
    while True:
        try:
          # Get the number of starting stones from the user and check
          # they have entered a number and it is with the bounds of 30 to 50
          stones = input("Choose a starting number of stones from 30 to 50: ")
          if stones.isdigit():
            stones=int(stones)
          else:
            print("  Error: You didn't enter a number.")
          if 30 <= stones <= 50:
            break
          else:
            print("  You must enter a number from 30 to 50.")  
        except Exception:
            print("  Please enter a number from 30 to 50.")
    # Display the number of starting stones the user provided
    print("")
    print("--------------------------------------")
    print(f"The number of starting stones is {stones}.")
    print("--------------------------------------")
    # Keep playing the game while the number of stones is not zero
    while stones != 0:
     #If player is not the AI Player 
     if player != 0:
      # If it is the human players turn then
      # make sure the players pick a number of stones between 1 and 3
      print(f"\n{curplayer.name} it is your turn.")
      check = True
      while check:
        try:
          stonesremoved = input("How many stones to remove? 1, 2 or 3? ")
          stonesremoved = int(stonesremoved)
          if 1 <= stonesremoved <= 3:
            stonesremoved=int(stonesremoved)
            check = False  
            break
          else:
            print("  Error: You didn't enter a number between 1 and 3.")  
        except Exception:
            print("  Error: Invalid input.")
            # If the user didn't enter an integer call the
            # function that generates a random number of stones
            randomstones()
      # Reduce the stones in the pile by what the user input  
      stones = int(stones) - int(stonesremoved)
      # Print a blank line then the number of remaining stones
      print("")  
      print("--------------------------------------")
      print(f"  There are {stones} stones remaining.") 
      print("--------------------------------------")
      # If the player has removed the last stone they win
      if stones == 0:
          print("")  
          print("************************************")   
          print("CONGRATULATIONS!")
          print(f"{curplayer.name} {curplayer.mitid} you have won!")
          print("************************************")         
          # Ask if the player wants to play again   
          # Parse the input and if invalid loop
          # Convert upper case Y and N to lower case for the check
          check = True
          while check:
            try:
              playagain = input("Do you want to play another game? (Y/N)?").lower()
              if not (playagain == "y" or playagain == "n"):
                print("Error: Y or N input required.") 
              else:
                check = False
            except Exception:
              print("  Error: Invalid input.")        
      # If there are stones left set incrment the human player details 
      if player == 1:
          curplayer.name = player2.name
          curplayer.mitid = player2.mitid
          player = 2
      elif player == 2:
          curplayer.name = player1.name
          curplayer.mitid = player1.mitid
          player = 0  
     else:
       # If it is the computer player turn,  
       # if there are 3 or less stones left, the computer
       # takes the last stones to win the game.
       if stones <= 3:
          print(f"\nI remove the remaining {stones} stones.")
          print("")
          print("Computer wins!!!")
          stones = 0
          # Ask if the player wants to play another game and
          # loop if the input isn't valid
          playagain =""      
          check = True
          while check:
            try:
              playagain = input("Do you want to play another game? (Y/N)?").lower()
              if not (playagain == "y" or playagain == "n"):
                print("Error: Y or N input required.") 
              else:
                check = False
            except Exception:
              print("  Error: Invalid input.")
       # If the remaining stones can be evenly divided by 3 remove two stones   
       # otherwise remove one stone 
       # I need to update variables to display them
       else:
          if stones % 3 == 0:
            stonesremoved = 2
            stones = stones - 2
          else:
            stonesremoved = 1
            stones = stones - 1
          # Tell the human players how many the computer removed  
          print(f"\nI remove {stonesremoved} stones.")
          print("\n--------------------------------------")
          print(f"  There are {stones} stones remaining.")  
          print("--------------------------------------")
       # Set the next player after the AI player:     
       player = 1
       curplayer.name = player1.name
       curplayer.mitid = player1.mitid
 else:
    # End the game.
      print("\n Thanks for playing NIM. Goodbye!")  
      
if __name__=="__main__":
    main()      

 