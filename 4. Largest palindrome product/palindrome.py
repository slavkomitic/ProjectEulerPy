def palindrome(digits=3):
	"""
	Finds the largest palindrome made from the product of two n-digit numbers.

	'A palindromic number reads the same both ways.
	The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.'
	"""
	number = int("9"*digits)
	lower_limit = int(number**(1/2))
	max_palindrome = 0

	for a in range(number, lower_limit, -1):
		for b in range(number, lower_limit, -1):
			n = str(a*b)
			if (n == n[::-1]) and int(n) > max_palindrome:
				max_palindrome = int(n)
	
	return max_palindrome



if __name__ == "__main__":
	print(palindrome(3))