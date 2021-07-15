def sumsquarediff(number_count=100):
	"""
	Returns the difference between the sum of the squares of the first <number_count> natural numbers and the square of the sum.
	"""
	def _sumofsquares(number_count):
		square_sum = 0
		for n in range(1, number_count+1):
			square_sum += n**2
		return square_sum

	def _squareofsum(number_count):
		number_sum = (number_count + 1) * (number_count/2)
		return number_sum**2


	return _squareofsum(number_count) - _sumofsquares(number_count)



if __name__ == '__main__':
	print(sumsquarediff(100))
