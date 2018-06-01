# Creates a list of numbers that pass the luhn test and outputs to a text file
# Cool! But you don't need it :(

import sys

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

def luhn_test(num):
	reversed_num_str = str(num)[::-1]
	s1 = sum([int(reversed_num_str[i]) for i in range(0, len(str(num)), 2)])
	s2 = sum([sum_digits(2*int(reversed_num_str[i])) for i in range(1, len(str(num)), 2)])
	return int(str(s1+s2)[::-1][0]) == 0

def luhn_generator(n):
	valid_numbers = []
	for x in range(n):
		if luhn_test(x):
			valid_numbers += [x]
	return valid_numbers

if __name__ == "__main__":
	upper_limit = input("Generate valid credit card numbers up to: ")
	luhn_nums = luhn_generator(upper_limit)

	orig_stdout = sys.stdout
	f = open('luhn_numbers.txt', 'w')
	sys.stdout = f

	for n in luhn_nums:
		print n

	sys.stdout = orig_stdout
	f.close()