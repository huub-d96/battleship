'''
This file contains the fucntions to draw the 
game on the screen and execute a turn for either
the human or computer player
'''

#Import libs
import os
import sys
import time
import random

#Import baord file
import boards

#Function to clear the screen (current: Linux/MacOs only)
def clear_screen():
    os.system('clear')

#Function to refresh the game screen
def refresh(my_board, op_board):
	banner ='''  
 ____        _   _   _           _     _       
|  _ \      | | | | | |         | |   (_)      
| |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  
|  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                        | |    
                                        |_|    
'''
    #Clear the screen
	clear_screen()

    #Print banner and current state of game
	print(banner)
	boards.show_boards(my_board, op_board)
    
#Human player's turn
def turn_player(my_board, op_board):

	playing = True
	while True:
	    #Get human input and check for errors
		while True:
			try:
			    row, col = input("Select coordinates [row col]: ").split(" ")
			    row = int(row)-1
			    col = ord(col) - ord('A')
			    break
			except KeyboardInterrupt: # Quit the game on interrupt                
			    print("\nGame exit")
			    sys.exit()
			except:
			    print("Invalid move. Try again")

        #Check if coordinate was hit or mis
		if op_board[row][col] == 1:
		    op_board[row][col] = 2
		    refresh(my_board, op_board)
		    print("Hit!")

		else:
		    op_board[row][col] = 3
		    refresh(my_board, op_board)
		    print("Miss!")            
		    break

        #Check if player has one by seeing if all boats are hit
		if 1 not in [b for sub_b in op_board for b in sub_b]:
		    print("You won!")
		    playing = False
		    break

    #Return bool to signal that the game is still being played
	return playing            

    
    
#Computers' turn
def turn_computer(my_board, op_board, t_sleep=2):

	playing = True
	while True:
	    print("Computer is thinking...")
	    time.sleep(t_sleep) #Add pause for player's convenience

	    #Get a random unused coordinate
	    while True:
	        row = random.randint(0,len(my_board)-1)
	        col = random.randint(0,len(my_board[0])-1)

	        if my_board[row][col] < 2:
	            break

	    #Check for hit or mis
	    if my_board[row][col] == 1:
	        my_board[row][col] = 2
	        refresh(my_board, op_board)
	        print("Computer hit your boat!")
     
	    else:
	        my_board[row][col] = 3
	        refresh(my_board, op_board)
	        print("Computer missed your boat!")            
	        break

        #Check if computer has won the game
	    if 1 not in [b for sub_b in my_board for b in sub_b]:
	        print("Computer won!")
	        playing = False
	        break

    #Return bool to signal that the game is still being played
	return playing

#Computer player's turn
def turn_computer_player(my_board, op_board, t_sleep=2):

	playing = True
	while True:
	    print("Computer is thinking...")
	    time.sleep(t_sleep) #Add pause for player's convenience

	    #Get a random unused coordinate
	    while True:
	        row = random.randint(0,len(op_board)-1)
	        col = random.randint(0,len(op_board[0])-1)

	        if op_board[row][col] < 2:
	            break

	    #Check for hit or mis
	    if op_board[row][col] == 1:
	        op_board[row][col] = 2
	        refresh(my_board, op_board)
	        print("Computer player hit opponnent's boat!")
	    else:
	        op_board[row][col] = 3
	        refresh(my_board, op_board)
	        print("Computer player missed opponent's boat!")            
	        break

        #Check if computer has won the game
	    if 1 not in [b for sub_b in op_board for b in sub_b]:
	        print("Computer player won!")
	        playing = False
	        break

    #Return bool to signal that the game is still being played
	return playing
	
