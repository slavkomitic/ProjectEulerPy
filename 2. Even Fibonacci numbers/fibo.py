def fibo(limit=4*10**6):
	"""
	sums up even-valued Fibonacci sequence numbers whose values do not exceed <limit>
	"""
	total = 2
	a, b = 1, 2

	while b < limit:
		a, b = b, a + b
		if b % 2 == 0:
			total += b

	return total

if __name__ == "__main__":
	print(fibo())