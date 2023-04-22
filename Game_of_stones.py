# Justin Thomas MIT211573
# 18th October 2021
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
#   playeronename is human player 1 name in title case
#   playertwoname is human player 2 name in title case
#   playeroneid is human player 1 student id in title case
#   playertwoid is human player 2 student id in title case
#   player is who the current player is 0 (computer), 1 or 2
#   stonesremoved is the number of stones removed by a player
#   check is used to set a condition to validate input
#   playername is the name of the current human player
#   playerid is the student number of the current human player
#
# Import the random library so we can use it to choose a random number
import random
# Set the initial number of stones
stones = 0
# Set the initial number of stones to remove
stonesremoved = 0
# Set player
player = 0
# Set the initial play state to playing
playagain = "y"
# define a global variable I can use outside the function. 
global check
# Introduce the game and the rules
# I've used a function here just to use one. Also used multi-line print.
def intro():
 print("This is the game of NIM. I am the AI player."
 "Each player in turn chooses a number of stones to remove from the pile."
 "The number removed must be between 1 and 3 stones."
 "The last player to remove stones wins!")
 
# Define a function to check if the user hasn't entered anything in text input
def checknullinput(x):
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
# a random number of stones between 1 and 3 inclusive
def nostonesremoved(y):
    global check
    if y == "":
        stonesremoved = int(random.choice([1,3]))
        print(f"Invalid input so a random {stonesremoved} stones removed")
        check = False
    else:
        check = False    
        
# Run the function to display the intro
intro()
# Set an initial state for the input checks
check = True
# Ask for the player names and store them in title case   
while check == True:
  playeronename = str(input("Enter the name of player 1: ").title())
  # use the function to check the user entered something
  checknullinput(playeronename)
  # Reset the check flag for the next check
check = True
while check:
   playeronemitid = str(input("Enter the MITID of player 1: ").title())
   checknullinput(playeronemitid)
check = True
while check:   
    playertwoname = str(input("Enter the name of player 2: ").title())
    checknullinput(playertwoname)
check = True
while check:     
    playertwomitid = str(input("Enter the MITID of player 2: ").title())
    checknullinput(playertwomitid)
check = True
# ======================================================================
# This is the main loop of the game
# It starts here so the players don't have to enter their details
# in again if they choose to play another game.
# While the playagain state is y continue to play
# ======================================================================
while playagain == "y":
    # Use randomisation to pick which human player will get the first turn
    # player = random.choice([1,2])
    player = random.choice([1,2])
    # Set the identity of the current player. I use these to display the
    # current player details while playing and if they win
    if player == 1:
        playername = playeronename
        playerid = playeronemitid
    elif player == 2:
        playername = playertwoname
        playerid = playertwomitid
    # Just a blank line
    print("")
    # Tell the player who goes first
    print(f"{playername} will have the first turn and pick the number of starting stones.")
    # Loop the request until a number of stones between 30 and 50 is entered
    # and catch invalid input
    while True:
        try:
          # Get the number of starting stones from the user and check
          # they have entered a number and it is with the bounds of 30 to 50
          stones = input("Choose a starting number of stones between 30 and 50: ")
          if stones.isdigit():
            stones=int(stones)
          else:
            print("You didn't enter a number.")
          if 30 <= stones <= 50:
            break
          else:
            print("You must enter a number between 30 and 50.")  
        except ValueError():
            print("You must enter a number between 30 and 50.")
    # Display the number of starting stones the user provided
    print(f"The number of starting stones is {stones}")
    # Keep playing the game while the number of stones is not zero
    while stones != 0:
     #If player is not the AI Player 
     if player != 0:
      # If it is the human players turn then
      # make sure the players pick a number of stones between 1 and 3    
      print(f"\n{playername} it is your turn.")
      print("You must choose between 1 and 3 stones to remove")
      while True:
        try:
          stonesremoved = input("How many stones to remove? 1, 2 or 3? ")
          if stonesremoved.isdigit():
            stonesremoved=int(stonesremoved)
            if 1 <= stonesremoved <= 3:
              break
            else:
              nostonesremoved(stonesremoved) 
              break
          else:
              nostonesremoved(stonesremoved)
              break
            #print("Error: You didn't enter a number.")
        except Exception:
              nostonesremoved(stonesremoved)
              break
      # If there is less than 3 stones left and the user tries to remove
      # more than there are just advise them they win.      
      if stones < stonesremoved:
        print("There aren't that many stones left.")
        print("But you remove the last stones and you win!")
        stones = 0
      else:
        # Otherwise reduce the stones in the pile by what the user input  
        stones = stones -  stonesremoved
      # Print a blank line then the number of remaining stones
      print("")  
      print(f"There are {stones} stones remaining.")     
      # If the player has removed the last stone they win
      if stones == 0:
          print(f"CONGRATULATIONS! {playername} {playerid} you have won!")
          # Ask if the player wants to play again   
          check= True
          while check:
            playagain = input("Do you want to play another game? (Y/N)?").lower()
            checknullinput(playagain)
      # If there are stones left set incrment the human player details 
      if player == 1:
          playername = playertwoname
          playerid = playertwomitid
          player = 2
      elif player == 2:
          playername = playeronename
          playerid = playeronemitid
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
          while not (playagain == "y" or playagain == "n"):
            playagain = input("Do you want to play another game? (Y/N)?").lower()
            if not (playagain == "y" or playagain == "n"):
              print("Error: Y or N input required.") 
            else:
              break  
       # If more than 3 stones play the optimal strategy that is remove 2 stones 
       # if the remaining stones can be evenly divided by 3 else remove one stone   
       else:
          if stones % 3 == 0:
            stonesremoved = 2
            stones = stones - 2
          else:
            stonesremoved = 1
            stones = stones - 1
          # Tell the human players how many the computer removed  
          print(f"\nI remove {stonesremoved} stones.")
          print(f"\nThere are {stones} stones remaining.")     
       # Set the next player after the AI player:     
       player = 1
       playername = playeronename
       playerid = playeronemitid
else:
    # End the game.
      print("\n Thanks for playing NIM. Goodbye!")  
 
 
