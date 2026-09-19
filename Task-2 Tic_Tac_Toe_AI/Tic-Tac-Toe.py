import math

# Create an empty board
board = [" " for _ in range(9)]


# Display Board
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check the game status
def check_game(b):
    winning_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for x, y, z in winning_patterns:
        if b[x] == b[y] == b[z] and b[x] != " ":
            return b[x]

    if " " not in b:
        return "Tie"

    return None


# Minimax Algorithm
def minimax(game_board, maximizing):
    result = check_game(game_board)

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Tie":
        return 0

    if maximizing:
        highest_score = -math.inf

        for position in range(9):
            if game_board[position] == " ":
                game_board[position] = "O"

                score = minimax(game_board, False)

                game_board[position] = " "

                highest_score = max(highest_score, score)

        return highest_score

    else:
        lowest_score = math.inf

        for position in range(9):
            if game_board[position] == " ":
                game_board[position] = "X"

                score = minimax(game_board, True)

                game_board[position] = " "

                lowest_score = min(lowest_score, score)

        return lowest_score


# Find the best move for the computer
def computer_move():
    best_score = -math.inf
    selected_position = 0

    for position in range(9):

        if board[position] == " ":
            board[position] = "O"

            score = minimax(board, False)

            board[position] = " "

            if score > best_score:
                best_score = score
                selected_position = position

    board[selected_position] = "O"


# Main Game
while True:

    display_board()

    player_input = int(input("Enter position (1-9): "))
    player_position = player_input - 1

    if board[player_position] != " ":
        print("Invalid Move")
        continue

    # Player's move
    board[player_position] = "X"

    result = check_game(board)

    if result:
        display_board()
        print("Winner:", result)
        break

    # Computer's move
    computer_move()

    result = check_game(board)

    if result:
        display_board()
        print("Winner:", result)
        break