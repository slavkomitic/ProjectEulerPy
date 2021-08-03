def latticepaths(gridsize):
	"""
	Starting in the top left corner of a 2×2 grid, 
	and only being able to move to the right and down, 
	there are exactly 6 routes to the bottom right corner.

	The function finds and returns how many such routes are there through a n×n grid
	"""
	result = 1
	for n in range(1, gridsize+1):
		result *= (gridsize+n)/n
	return round(result)
	

if __name__ == '__main__':
	print(latticepaths(20))