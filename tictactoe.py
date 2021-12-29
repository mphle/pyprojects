'''
Very simple tic tac toe game. First ever app build by myself! Very proud of it!~~
'''

from IPython.display import clear_output
import time


#Displaying GameBoard
def display_game(game_board):
    print(" {} | {} | {} ".format(game_board[7],game_board[8],game_board[9]))
    print("-----------")
    print(" {} | {} | {} ".format(game_board[4],game_board[5],game_board[6]))
    print("-----------")
    print(" {} | {} | {} ".format(game_board[1],game_board[2],game_board[3]))

#Checking For Winner
def check_win(game_board,player):
    win = False
    
    player = player.upper()
    
    if game_board[1] == player and game_board[2] == player and game_board[3] == player:
        win = True
    elif game_board[4] == player and game_board[5] == player and game_board[6] == player:
        win = True
    elif game_board[7] == player and game_board[8] == player and game_board[9] == player:
        win = True
    elif game_board[1] == player and game_board[4] == player and game_board[7] == player:
        win = True
    elif game_board[2] == player and game_board[5] == player and game_board[8] == player:
        win = True  
    elif game_board[3] == player and game_board[6] == player and game_board[9] == player:
        win = True
    elif game_board[1] == player and game_board[5] == player and game_board[9] == player:
        win = True 
    elif game_board[3] == player and game_board[5] == player and game_board[7] == player:
        win = True
    else:
        win = False
    if win == True:        
        print("Congratulations player {}, you have won the game!".format(player))
        
    return win

#User Prompt: Replay
def replay(): 
    replay = "wrong"
    question = "Do you want to keep playing (Y/N)?"
        
    while replay not in ["Y","N"]:
        replay = input(question).upper()
        
        print(replay)
        if replay not in ["Y","N"]:
            clear_output()
            print("Please choose Y or N. "+question)
            
            
        else:
            if replay == "Y":
                return True
            else:
                return False   

#User Prompt: X/O Choice
def player_choice():
    from IPython.display import clear_output

    player_choice = "wrong"

    while player_choice not in ["X","O"]:
        player_choice = input("Who wants to start? X or O? ").upper() 
        
        if player_choice not in ["X","O"]:
            clear_output()
            print("Please choose X or O.")
    
        else:
            if player_choice == "X":
                player1 = "X"
                player2 = "O"
            else:
                player1 = "O"
                player2 = "X"
    
    return ("",player1,player2)

#User Prompt: Next Move
def position_choice(game_board,player):

    position_range = range(1,10)
    position = "wrong" #assume falsly chosen input
    p_taken = True #assume it migh be taken
    
    while position not in position_range or p_taken == True:
        position = input("Player {} choose your next move (position 1-9):".format(player))
        
        try:#here it gets into the range
            position = int(position)
        except:
            pass
        
        if position not in position_range:
            print("Please choose position in between 1 and 9.")
        
        else:
            if game_board[position] not in [" "]:
                print("This position is already taken, please choose something different.")
                p_taken = True
            else:
                p_taken = False
                
        
    return position

#Game Intro
def game_tut():
    from IPython.display import clear_output
    import time
    
    print("This is the game board")
    
    game_board = [" "] * 10
    display_game(game_board)
    
    
    time.sleep(3)
    
    clear_output()
    
    print("These are the positions on the gameboard")
    game_board = [0,1,2,3,4,5,6,7,8,9]
    display_game(game_board)
    
    time.sleep(3)
    
    clear_output()
    
    print("Let's get started")
    time.sleep(2)    

#Reseting Game Board
def game_board_reset():
    global game_board
    game_board = [" "] * 10

#Marking Field
def mark_field(game_board,player,position):
    #print("Player {} selected position {}".format(player,position))
    game_board[position] = player.upper()

#Checking For Draw Situation
def check_draw(game_board):
    if game_board.count("O")+game_board.count("X")>=9:
        print("It looks like no one won this time!")
        return True
    else:
        return False

# Game Logic
def run_game(): 
    #Turorial
    #game_tut()

    #Still playing?
    game_on = True
    while game_on:

        #Reset board game
        game_board_reset()

        #Initioal set up
        player = player_choice()

        clear_output()
        display_game(game_board)



        win = False
        draw = False
        current_player = 1

        while win == False and draw == False:
            selected_position = position_choice(game_board,player[current_player])
            mark_field(game_board,player[current_player],selected_position)  
            
            time.sleep(0.1)
            clear_output()
            display_game(game_board)

            #Check for win
            win = check_win(game_board,player[current_player])
            
            #Check for draw
            draw = check_draw(game_board)

            #Alternate players
            if current_player == 1:
                current_player = 2
            elif current_player == 2:
                current_player = 1
        
        time.sleep(1)
        game_on = replay()
  
  
  #Launch the Game
  run_game()
