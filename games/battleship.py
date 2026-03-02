import random

#generate the board and print it. 
board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", "", " ", " ", " "]]
    
#create ships and size.
ships = { "  " : 2,"  " : 3,"  " : 4}
size = 5


# generate the random ships and their sizes.
for ship, L in ships.items():
    V_H = random.choice(['H', 'V'])
    if V_H == 'H':
        x = random.randint(0, size - L)
        y = random.randint(0, size - 1)
        for i in range(L):
            board[y][x + i] = ship
        
                
    else:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - L)
        for i in range(L):
            board[y + i][x] = ship
        
    
#Intro to the game:
print('Welcome to Battleship! Your goal is to hit all the hidden ships. Goodluck!')

#print game board with random ships.
def print_board():
    cols = '  1 2 3 4 5'
    rows = 'ABCDE'
    print(cols)
    for i in range(size):
        row = ' '.join(board[i])
        print(rows[i] + ' ' + row)

#to end the game if the user sinks all the ships      
def ships_sunk():
     for row in board:
        if any(cell in ships for cell in row):
            return False
     return True
    
#create the game aspect
def play_game():
    print_board()
    guess = input("Enter coordinates: ").upper()

    if len(guess) != 2 or not guess[0].isalpha() or not guess[1].isdigit():
        print("Invalid input.")


    x = int(guess[1]) - 1
    y = ord(guess[0]) - ord('A')

    if board[y][x] in ships:
        print("Hit!")
        board[y][x] = 'H'
        ship = board[y][x]
        
    elif board[y][x] == ' ':
        print("Miss!")
        board[y][x] = 'M'
    
    if not ships_sunk():
        play_game()
    else:
        print("Congratulations! You have sunk all the ships!")
         
play_game()


        



    


