def get_multiples(limit=1000):
	"""
	Finds & returns the sum of all the multiples of 3 or 5 below <limit>.
	"""
	return sum([n for n in range(limit) if (n % 3 == 0) or (n % 5 == 0)])

if __name__ == "__main__":
	print(get_multiples())
