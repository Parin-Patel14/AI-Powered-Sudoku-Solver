import time
def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

global recursion_counter
recursion_counter = 0
start_time = time.time()  # Initialize start time at the global level if it's used globally

def depth_limited_solve(board, depth, update_callback=None):
    global recursion_counter
    recursion_counter += 1

    if depth == 0:
        return None
    empty = find_empty(board)

    if not empty:
        end_time = time.time()
        result_info = '\nTotal recursive calls: {}\nTime taken to solve: {:.2f} seconds\n'.format(recursion_counter, end_time - start_time)
        print(result_info.strip())
        with open("sudoku_IDS_solver_output.txt", "a") as file:
            file.write(result_info)
        return board  # Solved

    row, col = empty
    for num in range(1, 10):  # Assuming Sudoku values range from 1-9
        if valid(board, num, (row, col)):
            board[row][col] = num
            if update_callback:
                update_callback(board, row, col, True)
            result = depth_limited_solve(board, depth - 1, update_callback)
            if result:
                return result
            board[row][col] = 0
            if update_callback:
                update_callback(board, row, col, False)

    return None

def iterative_deepening_solve(board, update_callback=None):
    depth = 81  # Start with a depth of 1
    while True:
        global start_time
        start_time = time.time()  # Reset start time for each depth level
        result = depth_limited_solve(board.copy(), depth, update_callback)
        if result:
            return result
        depth += 1  # Increase depth after each complete iteration

# Example callback function to show updates
def update_callback(board, row, col, is_placing):
    action = "Placing" if is_placing else "Removing"
    print(f"{action} number at position ({row}, {col})")