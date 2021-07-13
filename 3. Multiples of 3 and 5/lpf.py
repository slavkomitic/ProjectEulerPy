def largestprimefactor(number=600851475143):
	"""
	Returns the largest prime factor of the <number>
	"""
	def _isprime(n):
		cap_n = int(n**(1/2)) + 1
		if n == 2:
			return True

		for factor in range(2, cap_n): 
			if n % factor == 0:
				return False
		return True


	cap = int(number**(1/2)) + 1

	for factor in range(cap, 2, -1):
		if number % factor == 0 and _isprime(factor) :
			return factor


if __name__ == "__main__":
	print(largestprimefactor())

