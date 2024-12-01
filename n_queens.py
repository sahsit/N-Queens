from csp import nQueensCSP
from csp import print_board
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
        

def min_conflicts(csp, max_steps):
    current = csp

    print(f"Starting conflicted queens before any solution: {current.conflicted_queens}")

    for i in range(max_steps):
        T = len(current.variables) * 500 # set starting temperature high
        # cooling_rate = 0.95 # temperature should be decreased by T*0.95 every step
        
        # first, check if curr state is the solution
        if current.is_valid_solution():
            print(f"Solution found in {i} steps")
            return current

        
        # select a random conflicted queen (returns the column of that conflicted queen)
        var = select_conflicted_queen(current)
        # counts current number of conflicts to compare later
        
        
        current_conflicts = csp.conflicts(var)
                
        # find better position to put the queen (position that minimizes conflicts)
        new_value = find_better_position(current, var)
        # save the original column that the queen was in (to move it back later, if needed)
        original_value = csp.variables[var]
        
        # call move_queen to move the queen to "new_value" and update the row and diagonal conflicts
        current.move_queen(var, new_value)
        
        # count number of conflicts that we'd have if we moved the queen to the new position
        new_conflicts = csp.conflicts(var)
        
        # calculate difference between new and old conflicts
        delta = new_conflicts - current_conflicts
        
        # if the delta is less than 0, meaning the new_conflicts < current_conflicts...
        if delta <= 0:
            # ... then we move the queen to the new column because there's less conflicts
            current.update_conflicted_queens(var)
        else:
            # else, calculate whether we should move the queen or not using the SA formula (accepting worse solution with certain probability)
            if random.random() < math.exp(-delta/T):
                current.update_conflicted_queens(var)
            else:
                # if the new state had more conflicts AND it didn't choose it based on the SA formula, just stay where you are
                current.variables[var] = original_value
        
        # lower the temperature
        if len(current.conflicted_queens) < len(current.variables)//4:
            T *= 0.8
            
        # Print every 50 steps
        if i % 10000 == 0:  
            print(f"Step {i}: {len(current.conflicted_queens)} queens still in conflict (T={T:.2f})")
        
    # if the algo hasn't made any progress in max_steps, it restarts with another configuration 
    print("Restart due to no progress.")
    return min_conflicts(nQueensCSP(len(csp.variables)), max_steps)



def find_better_position(csp, var):

    
    n = len(csp.variables)
    min_conflicts = float('inf')
    best_positions = [] # list to store best candidates for positions  
    
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
                
        # update min_conflicts
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            best_positions = [row]
        elif conflicts == min_conflicts:
            # for rows with the same number of conflicts, they get added to a list
            best_positions.append(row)

    # the row choice is randomly picked from this list to maintain variability
    random_choice = random.choice(best_positions)

    return random_choice


    
def main():
    start_time = time.time()
    
    # creates instance of CSP with a certain nxn board
    csp = nQueensCSP(10000)

    # print all queens's positions on board
    print("starting positions: ", csp.variables)
    
    # print("queens in conflict in col 1: ", csp.conflicts(0)) 
    # print("queens in conflict in col 2: ", csp.conflicts(1)) 
    # print("queens in conflict in col 3: ", csp.conflicts(2)) 
    # print("queens in conflict in col 4: ", csp.conflicts(3)) 
    
    # call min_conflicts to solve the CSP
    solution = min_conflicts(csp, 10000)
    
    # print the queens's positions after board was solved
    if solution:
        print(solution.variables)
    end_time = time.time()
    # print_board(csp.variables)
    
    # should be nothing - set()
    print(f"Final conflicted queens: {csp.conflicted_queens}")

    
    # print("queens in conflict in col 1: ", csp.conflicts(0)) 
    # print("queens in conflict in col 2: ", csp.conflicts(1)) 
    # print("queens in conflict in col 3: ", csp.conflicts(2)) 
    # print("queens in conflict in col 4: ", csp.conflicts(3)) 
    
    
    print("solution check: ", csp.is_valid_solution())
    print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()