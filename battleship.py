from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def get_input_as_number(question):
    input = ""
    while input == "":
        try:
            input = raw_input(question)
            if input == "q":
                return 'q'
            input = int(input) - 1
        except ValueError:
            1 + 1
    return input
    
ship_row = random_row(board)
ship_col = random_col(board)

shouldContinue = True
for turn in range(5):
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    print "\n"
    print "TURN " + str(turn + 1)
    print "\n"
    guess_row = get_input_as_number("Guess Row (or q to quit):")
    if guess_row == "q":
        break
    guess_col = get_input_as_number("Guess Col (or q to quit):")
    if guess_col == "q":
        break
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            
        # On their last turn, show them where the battleship was
        if turn == 4:
            board[ship_row][ship_col] = "="
    print_board(board)
    turn = turn + 1
print "!!GAME OVER!!"

    

