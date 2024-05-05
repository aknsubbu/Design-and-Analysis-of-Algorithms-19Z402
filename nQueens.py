import time 

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))

def is_safe(board, row, col):
    for i in range(col):
        # this iterates thru the columns upto the column 'col' from the start
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            # if board[i] == row then it means that there is a queen in the same row
            # if board[i] -i == row-col it means that there is a queen in the same column
            # if board[i] + i == row + col then it means that there is a queen in the same diagonal
            return False
    return True

def solve_n_queens(n):
    # the backtrack function is a recursive function that tries to place a queen in each column
    # and then calls itself for the next column
    def backtrack(col):
        if col == n:
            solutions.append(list(board))
            return
        for row in range(n):
            if is_safe(board, row, col):
                # this is the place where the queen is placed in the board
                board[col] = row
                backtrack(col + 1)


    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

def solve_and_print_n_queens(n):
    solutions = solve_n_queens(n)
    for solution in solutions:
        # the below print statement reads the board and if the value in the column matches the value in the row then it prints the queen 
        # else it means that there is no queen in that cell and it prints a dot
        print_solution([[1 if solution[col] == row else 0 for col in range(n)] for row in range(n)])
        print()

if __name__ == '__main__':
    start = time.time()
    solve_and_print_n_queens(6)
    end = time.time()
    print("Time is:",end-start)