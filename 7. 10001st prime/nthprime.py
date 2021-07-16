def nthprime(n=10001):
	"""
	Finds and returns n-th prime number
	"""
	def _isprime(n):

		if str(n)[-1] == 0:
			print(n)

		cap_n = int(n**(1/2)) + 1
		if n == 2:
			return True

		for factor in range(2, cap_n): 
			if n % factor == 0:
				return False
		return True

	prime_counter = 1
	number = 3
	while True:
		if _isprime(number):
			prime_counter += 1
			if prime_counter==n:
				return number

		
		number += 2



if __name__ == '__main__':
	print(nthprime())