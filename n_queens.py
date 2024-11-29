from csp import nQueensCSP
from csp import print_board
import random
import time

def select_conflicted_queen(csp):
    # randomly selects conflicted queen to move for min_conflicts function
    if csp.conflicted_queens:
        #print(f"Conflicted queens: {csp.conflicted_queens}")
        return random.choice(list(csp.conflicted_queens))
    else:
        return None
        

def min_conflicts(csp, max_steps):
    current = csp
    
    for i in range(max_steps):
        if current.is_valid_solution():
            print(f"Solution found in {i} steps")
            return current

        
        
        # select a random conflicted queen
        var = select_conflicted_queen(current)
        
        if var is None:
            print("No conflicted queens left, but solution is invalid!")
            return None
        
        
        # store a better position for that queen in "value"
        value = find_better_position(current, var)
        # update its posiion in variables list
        current.variables[var] = value
        
        current.update_conflicted_queens(var)
            
        if i % 100 == 0:  # Print every 10 steps
            print(f"Step {i}: {len(current.conflicted_queens)} queens still in conflict")
        
    print("Restart due to no progress.")
    return min_conflicts(nQueensCSP(len(csp.variables)), max_steps)


def find_better_position(csp, var):
    n = len(csp.variables)
    min_conflicts = float('inf')
    best_positions = [] # list to store best candidates for positions  
    randomness = 0.1
    
    # loop through each row
    for row in range(n):
        # save the original row that the queen inhabits
        original_row = csp.variables[var]
        # update the queen's position to be the current row 
        csp.variables[var] = row
        # count the conflicts after moving the queen here
        conflicts = csp.conflicts(var)
        # move the queen back to its original row
        csp.variables[var] = original_row
        
        #print(f"Column {var}, Row {row}: Conflicts = {conflicts}")
        
        # update min_conflicts
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            best_positions = [row]
        elif conflicts == min_conflicts:
            # for rows with the same number of conflicts, they get added to a list
            best_positions.append(row)
            
    if random.random() < randomness:
        return random.randint(0, n - 1)
    
    #print(f"Best positions for column {var}: {best_positions}")
    # the row choice is randomly picked from this list to maintain variability
    return random.choice(best_positions)
    
def main():
    start_time = time.time()
    csp = nQueensCSP(40)
    

    print(csp.variables)
    num = select_conflicted_queen(csp)
    print("testing select_queen: ", num)
    num_conflicts= csp.conflicts(num)
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