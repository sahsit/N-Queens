from csp import nQueensCSP, print_board
import random
def select_conflicted_queen(csp):
    if csp.conflicted_queens:
        return random.choice(list(csp.conflicted_queens))
    else:
        return None
        
        




def main():
    csp = nQueensCSP(10000)

    print(csp.variables)
    num = select_conflicted_queen(csp)
    print("testing select_queen: ", num)
    num_conflicts= csp.conflicts(num)
    print("number of conflicts at col",num,": ", num_conflicts)
    #print_board(csp.variables)
    solution = csp.is_valid_solution()
    print("Is valid solution: ",solution)
    

if __name__ == "__main__":
    main()