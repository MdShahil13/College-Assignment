import random

def create_board():
    return [['~' for _ in range(5)] for _ in range(5)]

def print_board(board):
    print("  0 1 2 3 4")
    for row in range(5):
        print(f"{row} {' '.join(board[row])}")

def place_ship():
    ship_row = random.randint(0, 4)
    ship_col = random.randint(0, 4)
    return (ship_row, ship_col)

def play_game():
    board = create_board()
    ship_row, ship_col = place_ship()
    attempts = 0

    print("Welcome to Battleship!")
    print("Try to sink the ship. It's located somewhere on a 5x5 grid.")
    

    while True:
        print_board(board)
        
        try:
            row_guess = int(input("Enter the row (0-4): "))
            col_guess = int(input("Enter the column (0-4): "))
        except ValueError:
            print("Please enter valid integers between 0 and 4.")
            continue
        
        
        if row_guess < 0 or row_guess > 4 or col_guess < 0 or col_guess > 4:
            print("Invalid input. Please enter row and column between 0 and 4.")
            continue
        
        attempts += 1

        if (row_guess, col_guess) == (ship_row, ship_col):
            print("Congratulations! You hit the ship!")
            print(f"It took you {attempts} attempts to sink the ship.")
            if(attempts == 1):
                print("Excellent 😍😎")
            elif(1 < attempts <= 5):
                print("Good 😄😄")
            elif(5 < attempts <= 10):
                print("Average 😳😳")
            else:
                print("Very Bad 😏🙄")
                
            break
        else:
            print("You missed!")
            board[row_guess][col_guess] = 'X'

if __name__ == "__main__":
    play_game()
