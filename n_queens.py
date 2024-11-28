from csp import nQueensCSP, print_board
import random
import time
def select_conflicted_queen(csp):
    if csp.conflicted_queens:
        return random.choice(list(csp.conflicted_queens))
    else:
        return None
        
        




def main():
    start_time = time.time()
    csp = nQueensCSP(1000)
    end_time = time.time()

    print(csp.variables)
    num = select_conflicted_queen(csp)
    print("testing select_queen: ", num)
    num_conflicts= csp.conflicts(num)
    print("number of conflicts at col",num,": ", num_conflicts)
    #print_board(csp.variables)
    solution = csp.is_valid_solution()
    print("Is valid solution: ",solution)
    print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()