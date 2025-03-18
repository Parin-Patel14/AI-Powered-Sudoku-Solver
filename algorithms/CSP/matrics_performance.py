import re

def count_data(filename, data_to_count):
    total_count = 0
    count_occurrences = 0
    with open(filename, 'r') as file:
        for line in file:
            if data_to_count in line:
                match = re.search(r'\d+\.*\d*', line)
                if match:
                    count = float(match.group())
                    total_count += count
                    count_occurrences += 1
    return total_count, count_occurrences

def calculate_avg(filename, data_to_count):
    total, occurrences = count_data(filename, data_to_count)
    if occurrences != 0:
        avg = total / occurrences
    else:
        avg = 0
    return avg

filename = 'sudoku_CSP_solver_output.txt'  
data_to_count = ['Total recursive calls', 'Time taken to solve'] 

for data in data_to_count:
    avg = calculate_avg(filename, data)
    with open("matrics_performance.txt", "a") as file:
        file.write(f"Average {data}: {avg}\n")
    print(f"Average {data}: {avg}")

