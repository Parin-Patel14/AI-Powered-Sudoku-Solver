from copy import deepcopy
import collections
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

start_time = time.time()
recursion_counter = 0  # To count the number of iterations

def solve_bfs(board, callback=None):
    queue = collections.deque([(board, [])])
    seen_states = set()
    start_time = time.time()
    states_processed = 0

    while queue:
        current_board, path = queue.popleft()
        board_tuple = tuple(map(tuple, current_board))  # Convert board to a tuple of tuples for hashing

        if board_tuple in seen_states:
            continue
        seen_states.add(board_tuple)

        empty = find_empty(current_board)
        if not empty:
            end_time = time.time()
            print('Total states processed:', states_processed)
            print('Time taken to solve: {:.2f} seconds'.format(end_time - start_time))
            return True

        row, col = empty
        for num in range(1, 10):
            if valid(current_board, num, (row, col)):
                new_board = deepcopy(current_board)  # Use deepcopy here
                new_board[row][col] = num
                if tuple(map(tuple, new_board)) not in seen_states:
                    new_path = path + [(row, col, num)]
                    queue.append((new_board, new_path))
                    states_processed += 1
                    if callback:
                        callback(new_board, row, col, True)

    return False