from csp import nQueensCSP, print_board
import random
def select_conflicted_queen(csp):
    n = len(csp.variables)
    conflicted_queens = []

    for col in range(n):
        if csp.conflicts(col) > 0:
            conflicted_queens.append(col)
    if conflicted_queens:
        return random.choice(conflicted_queens)
    else:
        return None
        
        




def main():
    csp = nQueensCSP(8)

    print(csp.variables)
    num = select_conflicted_queen(csp)
    print("testing select_queen: ", num)
    num_conflicts= csp.conflicts(num)
    print("number of conflicts at col",num,": ", num_conflicts)
    print_board(csp.variables)
    solution = csp.is_valid_solution()
    print("Is valid solution: ",solution)
    

if __name__ == "__main__":
    main()