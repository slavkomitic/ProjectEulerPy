def pythagoreantriplet(number=1000):
	"""
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	a2 + b2 = c2
	For example, 32 + 42 = 9 + 16 = 25 = 52.

	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	The function finds the product abc where a + b + c = <number>
	"""
	a, b, c = 1, 1, 1

	def _is_triplet(x, y, z):
		"""checks if x2 + y2 = z2"""
		triplet = sorted((x,y,z))
		
		if ((triplet[0]**2 + triplet[1]**2 - triplet[2]**2) == 0):
			return True

	cap = number + 1
	triplets = set()
	for a in range(1, cap):
		for b in range(1, (cap - a)):
			for c in range(1, (cap - a - b)):
				if (a + b + c) == number and _is_triplet(a, b, c):
					return a * b * c

if __name__ == '__main__':
	print(pythagoreantriplet())