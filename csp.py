import random
import time

class nQueensCSP:
    def __init__(self, n):
        # n-queens is represented by a 1D list where each index is the column and the value at that index/column is the row that contains the queen
        #e.g. [0,2,1]
        #at column 0 the queen is in row 0
        #at column 1 the queen is in row 2
        #at column 2 the queen is in row 1
        self.n = n
        self.variables = [random.randint(0,n-1) for i in range (n) ]
        self.conflicted_queens = set()
        self.rows = {}
        self.rdiags = {}
        self.ldiags = {}
        self.conflicts_list = []
        
        for col in range(n):
            if self.conflicts(col) > 0:
                self.conflicted_queens.add(col)

        self.build_conflicts()

    def build_conflicts(self):
        self.rows = {}
        self.rdiags = {}
        self.ldiags = {}
        self.conflicts_list = []
        
        for col, row in enumerate(self.variables):
            # builds dictionaries for number of conflicts in rows, ldiagonal, and rdiagonal
            self.rows[row] = self.rows.get(row, -1) + 1 # updates conflicts in each row by searching for that row in the self.rows dictionary, if it doesn't exist yet, it returns -1
            self.rdiags[row - col] = self.rdiags.get(row - col, -1) + 1 
            self.ldiags[row + col] = self.ldiags.get(row + col, -1) + 1

        for col, row in enumerate(self.variables):
            conflict_count = (self.rows.get(row, 0) + self.rdiags.get(row - col, 0) + self.ldiags.get(row + col, 0))
            self.conflicts_list.append(conflict_count - 3) # subtract self count


    def update_conflicts(self, col, new_row):
        old_row = self.variables[col]

        # Remove old conflicts
        self.conflicts_list[col] = 0
        for col2, row2 in enumerate(self.variables):
            if col == col2:
                continue

            # Remove conflicts from old row
            if old_row == row2 or abs(old_row - row2) == abs(col - col2):
                self.conflicts_list[col2] -= 1

            # Add conflicts from new row
            if new_row == row2 or abs(new_row - row2) == abs(col - col2):
                self.conflicts_list[col2] += 1
                self.conflicts_list[col] += 1

            # Update the queen's position
            self.variables[col] = new_row
            
            

    
    def conflicts(self, col):
        #col 

        count = 0
        row = self.variables[col]
        n = len(self.variables)

        for col2 in range(n):
            row2 = self.variables[col2]
            #counts the amount of conflicting queens in the same row for the queen at col while ensuring it doesnt count the queen we are checking for
            if row2 == row and col2 != col:
                count+=1
            #counts diagonal conflicting queens
            if abs(row2 - row) == abs(col2 - col) and col2!= col:
                count+=1

        return count
    
    def update_conflicted_queens(self, col):
        
        #MUST USE THIS FUNCTION AFTER MOVING ANY QUEENS

        if self.conflicts(col) > 0:
            self.conflicted_queens.add(col)
        else:
            self.conflicted_queens.discard(col)
        
        #print(f"Updated conflicted queens: {self.conflicted_queens}")

    def is_valid_solution(self):
        if self.conflicted_queens:
            return False
        else:
            return True
    
    
def print_board(state):
    n = len(state)
    for row in range(n):
        row_string = ""
        for col in range(n):  
            if state[col] == row:
                row_string += "Q "
            else:
                row_string += ". "
        print(row_string.strip()) 
    




