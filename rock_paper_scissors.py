import random

# Define constants so we don't accidentally misspell these in our logic
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
POSSIBLE_MOVES = [ROCK, PAPER, SCISSORS]


def player1_wins(player1_move, player2_move):
    """
    Returns True if player1_move beats player2_move, or False if not.
    Note that this returns False in case of a tie!
    """
    if player1_move == ROCK and player2_move == SCISSORS:
        return True
    elif player1_move == PAPER and player1_move == ROCK:
        return True
    elif player1_move == SCISSORS and player2_move == PAPER:
        return True
    # TODO: finish the rest of this conditional logic 
    # DONE
    else:
        return False 


def is_valid_move(move):
    """
    Returns True if the move is considered valid input, or False if not.
    """
    if move in POSSIBLE_MOVES:
        return True
    else:
        return False
    # TODO: implement this function body
    # DONE


def play_rock_paper_scissors():
    # This randomly selects one of the options in POSSIBLE_MOVES
    computer_move = random.choice(POSSIBLE_MOVES)

    have_valid_move = False
    while not have_valid_move:
        print(f"choose from: {POSSIBLE_MOVES}")
        user_move = input('enter your move: ')
        if is_valid_move(user_move):
           have_valid_move = True
        # TODO: replace `pass` with the necessary logic
        
        else:
            print('invalid input, try again')

    print(f"computer's move: {computer_move}")
    if user_move == computer_move:  
        # TODO: replace `...` with the correct condition
        #DONE
        print("it's a tie!")
    elif player1_wins(user_move, computer_move):
        print('you win! 🏆🏆🏆')
    else:
        print('computer wins! 😭😭😭')

play_rock_paper_scissors()
