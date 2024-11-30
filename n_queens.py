from csp import nQueensCSP
from csp import print_board
# from csp import build_conflicts
# from csp import update_conflicts
# from csp import row_conflicts 
#from csp import nQueensCSP, print_board, row_conflicts
import random
import time
import math

def select_conflicted_queen(csp):
    # randomly selects conflicted queen to move for min_conflicts function
    if csp.conflicted_queens:
        #print(f"Conflicted queens: {csp.conflicted_queens}")
        return random.choice(list(csp.conflicted_queens))
    else:
        return None
        
        
def row_conflicts(csp, col):
    n = csp.n
    row_confs = [0 for _ in range(n)]

    for col_q, row_q in enumerate(csp.variables):
        if col_q == col:
            continue
        # Add conflicts for rows
        row_confs[row_q] += 1
        # Add conflicts for diagonals
        if 0 <= row_q + abs(col_q - col) < n:
            row_confs[row_q + abs(col_q - col)] += 1
        if 0 <= row_q - abs(col_q - col) < n:
            row_confs[row_q - abs(col_q - col)] += 1

    return row_confs


def min_conflicts(csp, max_steps):
    current = csp
    
    
    for step in range(max_steps):
        
        #T = len(csp.variables) * 1000 # starting temperature is 1000 (high)
        #cooling_rate = 1 - (i / max_steps) * 0.05 # temperature should be decreased by T*0.95 every step
        
        # first, check if curr state is the solution
        if current.is_valid_solution():
            print(f"Solution found in {step} steps")
            return current

        # select a random conflicted queen (returns the column of that conflicted queen)
        var = select_conflicted_queen(current)
        new_row = find_better_position(csp, var)
        
        csp.update_conflicts(var, new_row)
        
        
        
        
        
        
        # # counts current number of conflicts to compare later
        # current_conflicts = csp.conflicts(var)
                
        # # find better position to put the queen (position that minimizes conflicts)
        # new_value = find_better_position(current, var)
        # # store the original column that the queen was in
        # original_value = csp.variables[var]
        
        # # update the column of the queen to the new position we found with new_value
        # current.variables[var] = new_value
        # # count number of conflicts that we'd have if we moved the queen to the new pos
        # new_conflicts = csp.conflicts(var)
        
        # # calculate difference between new and old conflicts
        # delta = new_conflicts - current_conflicts
        
        # # if the delta is less than 0, meaning the new_conflicts < current_conflicts...
        # if delta <= 0:
        #     # ... then we move the queen to the new column because there's less conflicts
        #     current.update_conflicted_queens(var)
        # else:
        #     # else, calculate whether we should move the queen or not using the SA formula (accepting worse solution with certain probability)
        #     if random.random() < math.exp(-delta/T):
        #         current.update_conflicted_queens(var)
        #     else:
        #         # if the new state had more conflicts AND it didn't choose it based on the SA formula, just stay where you are
        #         current.variables[var] = original_value
        
        # # lower the temperature
        # T *= cooling_rate
            
        if step % 50 == 0:  # Print every 50 steps
            print(f"Step {step}: {sum(current.conflict)} queens still in conflict")
        
    print("Restart due to no progress.")
    return min_conflicts(nQueensCSP(len(csp.variables)), max_steps)


def find_better_position(csp, col):
    # n = len(csp.variables)
    # min_conflicts = float('inf')
    # best_positions = [] # list to store best candidates for positions  
    # randomness = 0.2
    
    # # loop through each row
    # for row in range(n):
        row_confs = row_conflicts(csp, col)
        min_conflicts = min(row_confs)
        best_positions = [row for row, conf in enumerate(row_confs) if conf == min_conflicts]
        return random.choice(best_positions)
        
        
        # # save the original row that the queen inhabits
        # original_row = csp.variables[var]
        # # update the queen's position to be the current row 
        # csp.variables[var] = row
        # # count the conflicts after moving the queen here
        # conflicts = csp.conflicts(var)
        # # move the queen back to its original row
        # csp.variables[var] = original_row
        
        # #print(f"Column {var}, Row {row}: Conflicts = {conflicts}")
        
        # # update min_conflicts
        # if conflicts < min_conflicts:
        #     min_conflicts = conflicts
        #     best_positions = [row]
        # elif conflicts == min_conflicts:
        #     # for rows with the same number of conflicts, they get added to a list
        #     best_positions.append(row)
            
    # if random.random() < randomness:
    #     return random.randint(0, n - 1)
    
    # #print(f"Best positions for column {var}: {best_positions}")
    # # the row choice is randomly picked from this list to maintain variability
    # return random.choice(best_positions)
    
def main():
    start_time = time.time()
    csp = nQueensCSP(50)
    

    print(csp.variables)
    num = select_conflicted_queen(csp)
    print("testing select_queen: ", num)
    num_conflicts = csp.conflicts_list[num]
    print("number of conflicts at col",num,": ", num_conflicts)
    solution = min_conflicts(csp, 500)
    if solution:
        print(solution.variables)
    end_time = time.time()
    #print_board(csp.variables)
    # solution = csp.is_valid_solution()
    # print("Is valid solution: ",solution)
    print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()