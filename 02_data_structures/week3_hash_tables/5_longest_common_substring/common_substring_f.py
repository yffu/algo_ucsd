# python3

import sys
from collections import namedtuple
# from random import randint

Answer = namedtuple('answer_type', 'i j len')


class Solver:
	def __init__(self, s, t):
		l_s = len(s)
		l_t = len(t)
		self.rev = False
		if l_s <= l_t:
			self.s, self.t = s, t
			self.l_s, self.l_t = l_s, l_t
		else:
			self.s, self.t = t, s
			self.l_s, self.l_t = l_t, l_s
			self.rev = True
		# precondition, s is always the shorter or same length string compared to t
		# 1000000007, 1000000009, 1000000000039, 1000000000061
		# self.m1 = 1000000007
		self.m1 = 1000000000039
		self.x = 263
		# self.x = randint(1, self.m1-1)
		self.xl1 = [1] * (self.l_s + 1)
		for i in range(1, self.l_s + 1):
			self.xl1[i] = (self.x * self.xl1[i - 1]) % self.m1


	def polyhash(self, str, m):
		answer = 0
		for c in reversed(str):
			answer = (answer * self.x + ord(c)) % m
		return answer

	def solve(self):
		# length of common substring ranges from 0 to length of s, shorter string
		# calculate length mid and see if common substring of length mid exists. if it does, expand search to
		answer = Answer(0, 0, 0)
		low, high = 0, self.l_s  # initialize so that s is always shorter string
		while low <= high:
			mid = (low + high) // 2
			ans_l = self.solve_l(mid)
			if ans_l:
				low = mid + 1
				answer = ans_l
			else:
				high = mid - 1
		return answer


	def solve_l(self, l):
		# 𝐻(𝑠𝑎𝑠𝑎+1 · · · 𝑠𝑎+𝑙−1) = ℎ[𝑎 + 𝑙] − 𝑥𝑙ℎ[𝑎]
		#  current best guess (i.e. the longest substring indices i, j and length)
		h_t = [0] * (self.l_t - l + 1)
		sub_t = self.t[self.l_t - l:]
		h_t[self.l_t - l] = self.polyhash(sub_t, self.m1)
		y = self.xl1[l]
		for i in reversed(range(0, self.l_t - l)):
			h_t[i] = (self.x * h_t[i + 1] + ord(self.t[i]) - y * ord(self.t[i + l])) % self.m1
		# convert h to dictionary of value : index
		d_t = {h_t[i]: i for i in range(len(h_t))}

		h_s = [0] * (self.l_s - l + 1)
		sub_s = self.s[self.l_s - l:]
		h_si = self.polyhash(sub_s, self.m1)
		if h_si in d_t:
			return Answer(d_t[h_si] if self.rev else self.l_s - l, self.l_s - l if self.rev else d_t[h_si], l)
		for i in reversed(range(0, self.l_s - l)):
			h_si = (self.x * h_si + ord(self.s[i]) - y * ord(self.s[i + l])) % self.m1
			h_s[i] = h_si
			if h_si in d_t:
				return Answer(d_t[h_si] if self.rev else i, i if self.rev else d_t[h_si], l)
		return None


for line in sys.stdin.readlines():
	s, t = line.split()
	solver = Solver(s, t)
	ans = solver.solve()
	print(ans.i, ans.j, ans.len)
