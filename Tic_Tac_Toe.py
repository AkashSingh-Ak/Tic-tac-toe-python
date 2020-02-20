###############################################################################
##############                                            #####################
##############    Tic Tac Toe game  Using Python IDLE     #####################
##############                                            #####################
###############################################################################

import random
import numpy as np


position = list(range(0, 9))


def Show() -> 'This function is to display the structure of tic tac toe':
    
    ## The Structure is similar to this

    #    0 | 1 | 2
    #   ----------
    #    3 | 4 | 5
    #   ----------
    #    6 | 7 | 8
    
    
    print(position[0], '|', position[1], '|', position[2])
    print('----------')
    print(position[3], '|', position[4], '|', position[5])
    print('----------')
    print(position[6], '|', position[7], '|', position[8])

def check(char, pos1, pos2, pos3):
    if position[pos1] == char and position[pos2] == char and position[pos3] == char:
        return 1   #  1 Represents True
                   #  0 Represents False

def Final_check(char)-> 'this Method is for all the possible outcomes for winning the game':
    if check(char, 0, 1, 2):
        return 1
    elif check(char, 3, 4, 5):
        return 1
    elif check(char, 6, 7, 8):
        return 1
    elif check(char, 0, 3, 6):
        return 1
    elif check(char, 1, 4, 7):
        return 1
    elif check(char, 2, 5, 8):
        return 1
    elif check(char, 0, 4, 8):
        return 1
    elif check(char, 2, 4, 6):
        return 1
    
def main_program():
    while 1:
        
        
        value = int(input("Select any position:  ")) 
        #Value contains the position entered by user

        if position[value] != 'X' and position[value] != 'O':
            position[value] = 'X'

            if Final_check('X') == 1:
                print("""                #####################################
                ####  Congrats  You  Win !! #########
                #####################################""")
                break
            

            flag = 1

            while flag:
                random.seed() # To generate random values 
                system = random.randint(0,8)

                if position[system] != 'X' and position[system] != 'O':
                    position[system] = 'O'

                    flag = 0

            if Final_check('O') == 1:
                print("""                #####################################
                #########   You  Lose!!   ###########
                #####################################""")
                break

                
        else:
            print('This position is already taken')

        Show()


if __name__ == '__main__':
    
    print('--------------------------------------------------------------------------------')
    print("############################# Welcome to Tic Tac Toe ###########################")
    print('--------------------------------------------------------------------------------')

    Show()
    main_program()
   
