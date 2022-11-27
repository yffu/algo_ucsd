# python3

import sys
debug = False


class Solver:
	def __init__(self, k, text, pattern):
		# t a string of length m
		# p a string of length n
		# p occurs in t at position i with at most k mismatches in p and t[i:i+p] differ in at most k positions
		self.k, self.t, self.p = k, text, pattern
		self.l_t = len(text)
		self.l_p = len(pattern)
		self.m1 = 1000000000039
		self.x = 263
		# Start by computing hash values of prefixes of 𝑡 and 𝑝 and their partial sums.
		# This allows you to compare any two substrings of 𝑡 and 𝑝 in expected constant time.
		self.h_t = [0] * (self.l_t + 1)
		self.h_p = [0] * (self.l_p + 1)
		self.xl = [1] * (self.l_p + 1)
		for i in range(1, self.l_p + 1):
			self.h_t[i] = (self.x * self.h_t[i - 1] + ord(self.t[i - 1])) % self.m1
			self.h_p[i] = (self.x * self.h_p[i - 1] + ord(self.p[i - 1])) % self.m1
			self.xl[i] = (self.x * self.xl[i - 1]) % self.m1
		for i in range(self.l_p + 1, self.l_t + 1):
			self.h_t[i] = (self.x * self.h_t[i - 1] + ord(self.t[i - 1])) % self.m1
		if debug:
			print('h_t: ', self.h_t, sep='')
			print('h_p: ', self.h_p, sep='')
			print('xl: ', self.xl, sep='')

		'''
		Try 1: Failed case #5/7: memory limit exceeded (Time used: 14.76/40.00, memory used: 2152353792/2147483648.)
		self.h_t = dict()
		self.h_p = dict()
		for l in reversed(range(1, self.l_p + 1)):
			y = self.xl[l]
			# hash values for text
			sub_t = self.t[self.l_t - l:]
			print('sub_t :', sub_t, sep='') if debug else None
			h_ti = self.polyhash(sub_t)
			print('h_ti :', h_ti, sep=', ') if debug else None
			self.h_t[(self.l_t - l, self.l_t - 1)] = h_ti
			for i in reversed(range(0, self.l_t - l)):
				h_ti = (self.x * h_ti + ord(self.t[i]) - y * ord(self.t[i + l])) % self.m1
				self.h_t[(i, i + l - 1)] = h_ti
			print('h_t: ', self.h_t, sep='') if debug else None
			# hash values for pattern
			sub_p = self.p[self.l_p - l:]
			print('sub_p :', sub_p, sep='') if debug else None
			h_pi = self.polyhash(sub_p)
			print('h_pi :', h_pi, sep=', ') if debug else None
			self.h_p[(self.l_p - l, self.l_p - 1)] = h_pi
			for i in reversed(range(0, self.l_p - l)):
				h_pi = (self.x * h_pi + ord(self.p[i]) - y * ord(self.p[i + l])) % self.m1
				self.h_p[(i, i + l - 1)] = h_pi
			print('h_p: ', self.h_p, sep='') if debug else None
		'''

	def solve(self):
		# For each candidate position 𝑖, perform 𝑘 steps of the form “find the next mismatch”.
		# append a start position(i) to an answer list if the substring starting from i of length len(pattern) has at most k mismatches
		# so for each substring of length len(pattern) starting at i, we need to count the number of mismatches
		answer = []
		for i in range(0, self.l_t - self.l_p + 1):
			# guaranteed that l_p is at least 1, if l_p = 1 then l = r is the base case.
			cnt = self.cnt_mismatch(i, i + (self.l_p - 1), i)
			print('mismatch count: ', cnt, sep='') if debug else None
			if cnt <= self.k:
				answer.append(i)
		return answer

	def cnt_mismatch(self, l, r, i):
		# mid, left, right substrings: if text matches pattern exactly then return
		# l=0, r=3, i=0
		h_ti = (self.h_t[r+1] - self.xl[r-l+1] * self.h_t[l]) % self.m1
		h_pi = (self.h_p[r-i+1] - self.xl[r-l+1] * self.h_p[l-i]) % self.m1
		print('left: ', l, 'right: ', r, 'i: ', i) if debug else None
		print('h_ti: ', h_ti, 'h_pi: ', h_pi) if debug else None
		if h_ti == h_pi:
			return 0
		else:
			# hashes of substring between text and pattern don't match
			if l == r:
				return 1
			else:
				m = (l+r)//2
				return self.cnt_mismatch(l, m, i) + self.cnt_mismatch(m+1, r, i)

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
