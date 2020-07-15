#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[2]:


#from IPython.display import clear_output

def display_board(board):
    
    print('      |      |      ')
    print('  '+board[1]+'   |   '+board[2]+'  |   '+board[3]+'   ')
    print('      |      |      ')
    print('--------------------')
    print('      |      |      ')
    print('  '+board[4]+'   |   '+board[5]+'  |   '+board[6]+'   ')
    print('      |      |      ')
    print('--------------------')
    print('      |      |      ')
    print('  '+board[7]+'   |   '+board[8]+'  |   '+board[9]+'   ')
    print('      |      |      ')
    


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[3]:


board = ['#','X','O','X','O','X','O','X','O','X']
display_board(board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**


def player_input():
    
    choice = 'wrong'
    while (choice != 'X' and choice != 'O'):
        choice = input("Player 1, Please choose 'X' or 'O'")
        
        if choice != 'X' and choice != 'O':
            print("Please enter 'X' or 'O'")
            print(type(choice))
            print(choice)
    
    if choice == 'X':
        return ('X','O')
    else:
        return('O','X')




# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**



def place_marker(board, marker, position):
    board[position] = marker
        
        


def win_check(board, mark):
    
    return (board[1]==mark and board[2]==mark and board[3]==mark
            (board[4]==mark and board[5]==mark and board[6]==mark) or
           (board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[1]==mark and board[4]==mark and board[7]==mark) or
           (board[2]==mark and board[5]==mark and board[8]==mark) or
           (board[3]==mark and board[6]==mark and board[9]==mark) or
           (board[1]==mark and board[5]==mark and board[9]==mark) or
           (board[7]==mark and board[5]==mark and board[3]==mark))
       
    
           



import random

def choose_first():
    return random.randint(1,2)



def space_check(board, position):
    
    return board[position] == ' '




def full_board_check(board):
    
    t=0
    for item in board:
        if item != ' ':
            pass
        else:
            t = t+1
    if t >= 1:
        return False
    else:
        return True
            
            


def player_choice(board):
    
    trigger = False
    while trigger == False:
        next_pos = int(input('input the next position to mark'))
        check = space_check(board, next_pos)
        
        if check:
            trigger = True
            return next_pos
        else:
            print('please input the blank position')
        
    




def replay():
    
    play_again = input("'Are you interested to play again. Press 'Y' or 'N'")
    return play_again




print('Welcome to Tic Tac Toe!')

while True:
    board = [" "," "," "," "," "," "," "," "," "," "]
    display_board(board)
    Player1_mark,Player2_mark =player_input()
    turn = choose_first()

    if turn == 1:
        print ('Player1 goes first')
    else:
        print ('Player2 goes first')
    
    game = input("Are you ready to play? if Yes, key 'Y' else 'N'")
    if game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 1:
            print ('player1')
            next_pos = player_choice(board)
            place_marker(board, Player1_mark, next_pos)
            display_board(board)
            if win_check(board, Player1_mark):
                print('Player1 won')
                display_board(board)
                game_on = False
            elif full_board_check(board):
                print('game drawn')
                display_board(board)
            else:
                print('player 2 turn')
                turn = 2
        else:
            print('player2')
            next_pos = player_choice(board)
            place_marker(board, Player2_mark, next_pos)
            display_board(board)
            if win_check(board, Player2_mark):
                display_board(board)
                print('Player2 won')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print('game drawn')
            else:
                print('player 1 turn')
                turn = 1

        
    play_again = replay()
    if play_again != 'Y':
        break
    else:
        pass





