def check_double(list):
    return all([list.count(x) <= 1 for x in range(1,10)])

def check_form(grid):
    if len(grid) != 9 or type(grid) is not list:
        return False
    for row in grid:
        if len(row) != 9 or type(row) is not list:
            return False
        for item in row:
            if item not in range(10):
                return False
    return True

def check_sudoku(grid):
    if not check_form(grid):
        return None
    for row in grid: #1
        if check_double(row):
            return False
    for i in range(9): #2
        temp = []
        for row in grid:
            temp.append(row[i])
        if check_double(temp):
            return False
    for row in [0, 3, 6]: #3
        for col in [0, 3, 6]:
	    temp = []
	    for n in range(3):
	        for m in range(3):
		   temp.append(grid[row+n][col+m])
		if check_double(temp):
		 return    False
    return True



def solve_sudoku(grid):
	import collections
	import copy
	import random
	if not check_form(grid):
		return None
	if not check_sudoku(grid):
		return False
	d = collections.defaultdict(list)
	print grid
	for row in range(9):
		for col in range(9):
			temp = copy.deepcopy(grid)
			if grid[row][col] == 0:
				for n in range(1, 10):
					temp[row][col] = n
					if check_sudoku(temp):
						d[(row, col)].append(n)
	def solve_rec(grid, d):				
		results = copy.deepcopy(grid)
		for row in range(9):
			for col in range(9):
				if results[row][col] == 0:
					for value in d[(row, col)]:
						results[row][col] = value
						new = solve_rec(results, d)
						if new is not False:
							return new
					return False
		return results
	
	return solve_rec(grid, d)


	
	



	



	

ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]



print solve_sudoku(ill_formed) # --> None
print solve_sudoku(valid)      # --> True
print solve_sudoku(invalid)    # --> False
print solve_sudoku(easy)       # --> True
print solve_sudoku(hard)       # --> True
