"""
File: largest_digit.py
Name: Livia Tseng 曾迺芩
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: Any integer that user input.
	:return: The largest digit in the integer.
	"""
	the_biggest = 0
	if n < 0:
		n = -n
	ans = helper(n, the_biggest)
	return ans


def helper(n, the_biggest):
	"""
	The helper function for find_largest_digit(n).
	:param n: The given number from find_largest_digit(n).
	:param the_biggest: Default = 0, using for storing the largest number when comparing.
	:return: The biggest digit in param n.
	"""
	if n == 0:
		return the_biggest
	else:
		single_digit = n % 10
		if single_digit > the_biggest:
			the_biggest = single_digit
		n = int((n - single_digit)/10)
		return helper(n, the_biggest)


if __name__ == '__main__':
	main()
