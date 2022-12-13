'''
File that contains some functions for
the boards of the game
'''

#Import libraries
import random
import string

#Function to generate board with random ship positions
def generate_board(size=10, ship_lengths = [4,3,3,2,2,2,1,1,1,1]):

    #Initialize board with zeros
    board = [[0]*size for _ in range(size)]

    #Place ships
    for length in ship_lengths:
        while True: #Try to fit boat here
            row = random.randint(0,size-1) #Row start
            col = random.randint(0,size-1) #Col start
            grw = random.randint(0,1)      #Grow direction
            
            collision = False
            for i in range(length):
                row_check = row+i*grw
                col_check = col+i*(1-grw)

                #Check out of bounds
                if row_check < 0 or row_check > size -1 or col_check < 0 or col_check > size-1:
                    collision = True
                    break
                
                #Check if boat collides with other boat
                if board[row_check][col_check] == 1:
                    collision = True
                    break

            if collision:
                continue

            #Place boat
            for i in range(length):
                board[row+i*grw][col+i*(1-grw)] = 1

            break

    #Return board with ships
    return board
            
#Print a board on the screen, without formatting it for players view
def print_board(board):
    print("  ",*string.ascii_uppercase[:len(board[0])],"")
    for i, p in enumerate(board):
        print(f'{i+1:2d}',"",end="")
        print(*p,"")

#Return a char which marks the current coordinate for the player
def get_marker(value):
    if value == 2:      #Hit
        return 'X'
    elif value == 3:    #Miss
        return 'O'
    else:               #Undiscoverd
        return '.'

#Show the board state for the player, only shows hits, misses and undiscovered coordinates
def show_boards(my_board, op_board):

    #Seperations between boards
    sep = " "*3

    #Alpabetical labels for the board columns
    col_labels = string.ascii_uppercase[:len(my_board[0])]

    #Print the current board states
    print("  ", "My moves", " "*(2*len(my_board[0])-len("My moves"))+sep, "Opponent's moves\n")
    print("  ", *col_labels, sep, " ", *col_labels)

    #Loop over rows
    for i in range(len(my_board)):
        print(f'{i+1:2d}',"",end="")

        #Columns for the first board
        for j in range(len(my_board[0])):
            marker = get_marker(op_board[i][j])
            print(marker,"",end="")
        print(sep, end="")

        #Columns for the second board
        print(f'{i+1:2d}',"",end="")
        for j in range(len(my_board[0])):
            marker = get_marker(my_board[i][j])
            print(marker,"",end="")

        #Newline    
        print("")
    #Newline
    print("")
