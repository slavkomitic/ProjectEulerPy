def summationofprimes(limit=2*10**6):
	"""
	Finds the sum of all the primes below <limit>.
	"""

	def _isprime(n):
		cap_n = int(n**(1/2)) + 1
		if n == 2:
			return True

		for factor in range(2, cap_n): 
			if n % factor == 0:
				return False
		return True

	return sum(filter(_isprime, range(2, limit + 1)))

if __name__ == '__main__':
	print(summationofprimes())