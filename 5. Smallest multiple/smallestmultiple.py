def smallestmultiple(divisors_limit=20):
	"""
	Returns the smallest positive number that is evenly divisible by all of the numbers from 1 to <divisors_limit>

	'2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.'
	"""
	def _isprime(n):
		cap_n = int(n**(1/2)) + 1
		if n == 2:
			return True

		for factor in range(2, cap_n): 
			if n % factor == 0:
				return False
		return True

	primes = set()
	
	for n in range(4, divisors_limit + 1):
		if _isprime(n):
			primes.add(n)

	two_powers = 0
	while 2**(two_powers+1) < divisors_limit:
		two_powers += 1

	three_powers = 0
	while 3**(three_powers+1) < divisors_limit:
		three_powers += 1

	product = 2**two_powers * 3**three_powers

	for n in primes:
		product *= n

	return product


if __name__ == '__main__':
	print(smallestmultiple(20))
