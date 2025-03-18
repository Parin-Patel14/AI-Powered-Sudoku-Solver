import time
recursion_counter = 0
start_time = time.time()
def solve(board, update_callback=None):
    global recursion_counter
    recursion_counter += 1

    empty = find_empty(board)
    if not empty:
        print('Total recursive calls:', recursion_counter)
        end_time = time.time()
        print('Time taken to solve: {:.2f} seconds'.format(end_time - start_time))
        with open("sudoku_solver_output.txt", "a") as file:
            file.write('\nTotal recursive calls: {}\n'.format(recursion_counter))
            file.write('Time taken to solve: {:.2f} seconds\n'.format(end_time - start_time))
        return True  
    row, col = empty

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
            if update_callback:
                update_callback(board, row, col, True)  
            
            if solve(board, update_callback):
                return True
            
            board[row][col] = 0
            if update_callback:
                update_callback(board, row, col, False) 
    
    return False

#Constraints
def valid(board, num, pos, count_false=None):
    
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x, box_y = pos[1] // 3, pos[0] // 3
    for i in range(box_y * 3, (box_y + 1) * 3):
        for j in range(box_x * 3, (box_x + 1) * 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def forward_check(board, row, col, num):
    related_cells = get_related_cells(row, col)
    for (r, c) in related_cells:
        if board[r][c] == 0 and not any(valid(board, potential_num, (r, c)) for potential_num in range(1, 10) if potential_num != num):
            return False
    return True

def get_related_cells(row, col):
    cells = set()
    for i in range(9):
        cells.add((row, i))
        cells.add((i, col))
    box_x, box_y = col // 3 * 3, row // 3 * 3
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            cells.add((i, j))
    cells.discard((row, col))
    return cells
