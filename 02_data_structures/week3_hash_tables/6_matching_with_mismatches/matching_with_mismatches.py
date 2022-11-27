# python3

import sys

class Solver:
	def __init__(self, k, text, pattern):
		self.k, self.t, self.p = k, text, pattern
		self.l_t = len(text)
		self.l_p = len(pattern)
		self.m1 = 1000000000039
		self.x = 263
		self.xl = [1] * (self.l_p + 1)
		for i in range(1, self.l_p + 1):
			self.xl[i] = (self.x * self.xl[i - 1]) % self.m1
		# substring range from length 0 to l_p
		self.h_t = dict()
		self.h_p = dict()
		# l = self.l_p
		for l in reversed(range(1, self.l_p + 1)):
			y = self.xl[l]
			# hash values for text
			sub_t = self.t[self.l_t - l:]
			print('sub_t :', sub_t, sep='')
			h_ti = self.polyhash(sub_t)
			print('h_ti :', h_ti, sep=', ')
			self.h_t[(l, self.l_t - l)] = h_ti
			for i in reversed(range(0, self.l_t - l)):
				h_ti = (self.x * h_ti + ord(self.t[i]) - y * ord(self.t[i + l])) % self.m1
				self.h_t[(l, i)] = h_ti
			print('h_t: ', self.h_t, sep='')
			# hash values for pattern
			sub_p = self.p[self.l_p - l:]
			print('sub_p :', sub_p, sep='')
			h_pi = self.polyhash(sub_p)
			print('h_pi :', h_pi, sep=', ')
			self.h_p[(l, self.l_p - l)] = h_pi
			for i in reversed(range(0, self.l_p - l)):
				h_pi = (self.x * h_pi + ord(self.p[i]) - y * ord(self.p[i + l])) % self.m1
				self.h_p[(l, i)] = h_pi
			print('h_p: ', self.h_p, sep='')

	def solve(self):
		# t a string of length m
		# p a string of length n
		# p occurs in t at position i with at most k mismatches in p and t[i:i+p] differ in at most k positions

		# compute hash values of prefixes of t and p and their partial sums.
		return []

	def polyhash(self, str):
		answer = 0
		for c in reversed(str):
			answer = (answer * self.x + ord(c)) % self.m1
		return answer


for line in sys.stdin.readlines():
	k, t, p = line.split()
	solver = Solver(int(k), t, p)
	ans = solver.solve()
	print(len(ans), *ans)
