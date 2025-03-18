import time
def valid(board, num, pos):
    for i in range(9): 
        if board[pos[0]][i] == num and pos[1] != i: 
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

recursion_counter = 0
start_time = time.time()
def solve_dfs(board, callback=None):
    global recursion_counter
    recursion_counter += 1

    empty = find_empty(board)
    if not empty:
        print('Total recursive calls:', recursion_counter)
        end_time = time.time()
        print('Time taken to solve: {:.2f} seconds'.format(end_time - start_time))
        with open("sudoku_DFS_solver_output.txt", "a") as file:
            file.write('\nTotal recursive calls: {}\n'.format(recursion_counter))
            file.write('Time taken to solve: {:.2f} seconds\n'.format(end_time - start_time))
        return True  
    row, col = empty

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
            if callback:
                callback(board, row, col, True) 
            if solve_dfs(board, callback):
                return True
            board[row][col] = 0 
            if callback:
                callback(board, row, col, False)  
    return False