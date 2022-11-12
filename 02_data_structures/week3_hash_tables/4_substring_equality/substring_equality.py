# python3

import sys
from random import randint
debug = False


class Solver:
	def __init__(self, str):
		self.str = str
		self.m1 = 1000000007
		self.m2 = 1000000009
		self.x = randint(1, 1000000000)
		self.h1 = [0] * len(str)
		self.h2 = [0] * len(str)
		self.xl1 = [1] * len(str)
		self.xl2 = [1] * len(str)
		for i in range(1, len(str)):
			self.h1[i] = (self.x * self.h1[i - 1] + ord(str[i - 1])) % self.m1
			self.h2[i] = (self.x * self.h2[i - 1] + ord(str[i - 1])) % self.m2
			self.xl1[i] = (self.x * self.xl1[i - 1]) % self.m1
			self.xl2[i] = (self.x * self.xl2[i - 1]) % self.m2

	def ask(self, i1, i2, l):
		# Recall also that when computing 𝐻(𝑠) mod 𝑚 it is important to
		# take every intermediate step (rather then the final result) modulo 𝑚.
		# (a ⋅ b) mod m = [(a mod m) ⋅ (b mod m)] mod m
		if debug:
			xl1_it = 1
			xl2_it = 1
			xl1_pow = pow(self.x, l) % self.m1
			xl2_pow = pow(self.x, l) % self.m2
			for i in range(l):
				xl1_it = (xl1_it * self.x) % self.m1
				xl2_it = (xl2_it * self.x) % self.m2
		if debug:
			print('xl1 iterated: ', xl1_it, sep=' ,')
			print('xl2 iterated: ', xl2_it, sep=' ,')
			print('xl1 power: ', xl1_pow, sep=' ,')
			print('xl2 power: ', xl2_pow, sep=' ,')
			print('xl1 pre-gen: ', self.xl1[l], sep=' ,')
			print('xl2 pre-gen: ', self.xl2[l], sep=' ,')

		i1h1 = (self.h1[i1 + l] - self.xl1[l] * self.h1[i1]) % self.m1
		i2h1 = (self.h1[i2 + l] - self.xl1[l] * self.h1[i2]) % self.m1
		i1h2 = (self.h2[i1 + l] - self.xl2[l] * self.h2[i1]) % self.m2
		i2h2 = (self.h2[i2 + l] - self.xl2[l] * self.h2[i2]) % self.m2
		return i1h1 == i2h1 and i1h2 == i2h2

		'''
		Try 1 - too slow
		x_pow_l = pow(self.x, l)
		i1h1 = (self.h1[i1 + l] - x_pow_l * self.h1[i1]) % self.m1
		i2h1 = (self.h1[i2 + l] - x_pow_l * self.h1[i2]) % self.m1
		if i1h1 == i2h1:
			i1h2 = (self.h2[i1 + l] - x_pow_l * self.h2[i1]) % self.m2
			i2h2 = (self.h2[i2 + l] - x_pow_l * self.h2[i2]) % self.m2
			return i1h2 == i2h2
		return False
		'''
		# Naive
		# return s[a:a+l] == s[b:b+l]


# read text to match from first line
str = sys.stdin.readline()
# read number of queries from second line
q = int(sys.stdin.readline())
# instantiate the solver
solver = Solver(str)
for i in range(q):
	# i1 is index of char of first substring,  i2 is index of char of second substring, l is length of substring
	i1, i2, length = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(i1, i2, length) else "No")
