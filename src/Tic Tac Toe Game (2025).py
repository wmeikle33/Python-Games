import os
from sys import exit
from IPython.display import clear_output
board = ['0','1','2','3','4','5','6','7','8','9','10']

def display_board(board):
    clear_output()
    print(board[7]+'|'+ board[8] + '|'+ board[9])
    print(board[4]+'|'+ board[5] + '|'+ board[6])
    print(board[1]+'|'+ board[2] + '|'+ board[3])
    os.system('clear')

def player_input():
    
    print('Welcome to Tic Tac Toe!')
    os.system('clear')
    
    marker = ''
    global player1
    global player2
    global turn
    while marker != 'X' and marker != '0':
        marker = input('Player 1, do you want to be X or 0?: ')
        os.system('clear')
        player1 = marker
    
    if player1 == 'X':
        print('Player 1 will go first')
        print("Player1, it's your turn")
        display_board(board)
        player2 = '0'
        turn = player1
    else:
        player2 = 'X'
        print('Player 2 will go first')
        print("Player2, it's your turn")
        display_board(board)
        turn = player2

def player_choice():
    choice = 'wrong'
    acceptable_range = range(0,10)
    within_range = False
    choice_free = False
    global position
    while choice.isdigit() == False or within_range == False or choice_free == False:
        choice = input("Please enter a number (1-9):")
        if choice.isdigit() == False:
            print('Sorry that is not a digit!')
            choice.isdigit() == False
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                if board[int(choice)].isdigit() == False:
                    print('That position is already taken, please choose another')
                    choice_free = False
                else:
                    within_range = True
                    choice_free = True
                    position = int(choice)
            else:
                print('Sorry, you are out of the acceptable range (1-9)')
                os.system('clear')
                within_range = False

def win_check(board):
    global game_on
    for i in range(1,10,3)
        if all(item == 'X' for item in board[i:i+3]:
                print('Player1 Wins!')
                os.system('clear')
                gameon_choice()
        elif board[i] == board[i+3] == board[i+6] == player1 == 'X':
                print('Player1 Wins!')
                os.system('clear')
                gameon_choice()
        elif all(item == '0' for item in board[i:i+3]:
                print('Player2 Wins!')
                os.system('clear')
                gameon_choice()
        elif board[i] == board[i+3] == board[i+6] == player1 == '0':
                print('Player2 Wins!')
                os.system('clear')
                gameon_choice()
    if '1' not in board and '2' not in board and '3' not in board and '4' not in board and '5' not in board and '6' not in board and '7' not in board and '8' not in board and '9' not in board:
        print("It's a tie!, Want to play again?")
        os.system('clear')
        gameon_choice()
   

def replacement_choice(board):
    user_placement = str(input('Type a string to place at position, X or 0:'))
    global position
    global turn
    while player1 == turn:
        if len(user_placement) > 1:
            print('That is not an appropriate choice, please choose X or O, X if you are player1, 0 if you are player2')
            replacement_choice(board)
        elif 'X' in user_placement:
            board[position] = user_placement
            display_board(board)
            win_check(board)
            print("Player 2, it's your turn")
            turn = player2
            player_choice()
            replacement_choice(board)
        else:
            print('That is not an appropriate choice, please choose X or O, X if you are player1, 0 if you are player2')
            os.system('clear')
            replacement_choice(board)
    while player2 == turn:
        if len(user_placement) > 1:
            print('That is not an appropriate choice, please choose X or O, 0 if you are player1, X if you are player2')
            os.system('clear')
            replacement_choice(board)
        elif '0' in user_placement:
            board[position] = user_placement
            display_board(board)
            win_check(board)
            print("Player 1, it's your turn")
            turn = player1
            player_choice()
            replacement_choice(board)
        else:
            print('That is not an appropriate choice, please choose X or O, X if you are player1, 0 if you are player2')
            os.system('clear')
            replacement_choice(board)

def gameon_choice():
    global board
    global game_on
    choice = input('Keep playing? Y or N ')
    if choice not in ['Y', 'N']:
        print("Sorry I don't understand! Please choose Y or N ")
        gameon_choice()
    elif choice == 'Y':
        os.system('clear')
        board = ['0','1','2','3','4','5','6','7','8','9','10']
        player_input()
        player_choice()
        replacement_choice(board)
    elif choice == 'N':
        print('The game is over')
        os.system('clear')
        exit()
    

def game_start():
    global game_on
    game_on = True
    while game_on == True: 
        board = ['0','1','2','3','4','5','6','7','8','9','10']
        player_input()       
        player_choice()
        replacement_choice(board)

game_start()
