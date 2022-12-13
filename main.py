'''
Simple battleship game in the terminal
* Play yourself or let computer play against itself
* Current game is set as a 10x10 board with 5 ships each
* Boats can be placed next no eachother, i.e. no gaps
* Lot's of features could be implemented to enhance gameplay
  but this is currently not needed for this proof-of-concept

Author: Huub Donkers
Date: 13-12-2022
'''
#Import libraries
import sys

#Custom libraries
import boards
import turns

def main():
    #Generate boards
    ship_lengths = [5, 4, 3, 3, 2]
    my_board = boards.generate_board(ship_lengths=ship_lengths)
    op_board = boards.generate_board(ship_lengths=ship_lengths)

    #Menu to select if the player plays himself or let the computer do it
    turns.clear_screen()
    print('''
     ____        _   _   _           _     _       
    |  _ \      | | | | | |         | |   (_)      
    | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  
    |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
    |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                            | |    
                                            |_|    
    Select play mode:
    1. Player vs computer
    2. Computer vs computer
    3. Exit
    ''')
    while True:
        try:
            selection  = int(input("Select : "))
            if selection == 1 or selection == 2 :
                break
            elif selection == 3:
                sys.exit()
            else:
                print("Menu item doesn't exist. Try again")

        except SystemExit:      
            print("Game exit")
            sys.exit()  
        except KeyboardInterrupt: # Quit the game on interrupt                
            print("\nGame exit")
            sys.exit()
        except:
            print("Invalid input. Please provide a menu number")

       
    #Setup intial screen
    turns.refresh(my_board, op_board)

    #Start the game    
    while(True):

        #Turn player 1
        if selection == 1: #Human player
            playing = turns.turn_player(my_board, op_board)
        elif selection == 2: #Computer player
            playing = turns.turn_computer_player(my_board, op_board, 0.75)

        if not playing:
            break

        #Turn player 2    
        playing = turns.turn_computer(my_board, op_board, 0.75)

        if not playing:
            break

    #Game finished!

if __name__ == "__main__":
   main()
