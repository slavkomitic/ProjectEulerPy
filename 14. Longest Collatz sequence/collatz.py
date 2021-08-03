def collatz(limit=10**6):
	"""
	The following iterative sequence is defined for the set of positive integers:

	n → n/2 (n is even)
	n → 3n + 1 (n is odd)

	Using the rule above and starting with 13, we generate the following sequence:

	13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
	It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it 	is thought that all starting numbers finish at 1.

	The function finds the starting number, under one <limit>, which produces the longest chain.
	"""

	def _calc_odd(n):
		return 3*n + 1

	def _calc_even(n):
		return n/2

	counter = 0
	number = limit
	max_chain = 0
	while number > 1:
		next_term = number
		while next_term != 1:
			counter += 1
			next_term = _calc_odd(next_term) if next_term % 2 else _calc_even(next_term)
		if counter > max_chain:
			max_chain = counter
			max_chain_number = number		
		counter	= 0
		number -= 1

	return max_chain_number


if __name__ == '__main__':
	print(collatz())