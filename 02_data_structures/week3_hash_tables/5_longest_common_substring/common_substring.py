# python3

import sys
from collections import namedtuple
from random import randint

Answer = namedtuple('answer_type', 'i j len')
debug = False

class Solver:
	def __init__(self, s, t):
		self.s = s
		self.t = t
		self.m1 = 1000000007
		self.m2 = 1000000009
		self.x = randint(1, self.m1-1)
		self.l_s, self.l_t = len(s)+1, len(t)+1
		self.h1s, self.h2s = [0] * self.l_s, [0] * self.l_s
		self.h1t, self.h2t = [0] * self.l_t, [0] * self.l_t
		self.xl1, self.xl2 = [1] * max(self.l_s, self.l_t), [1] * max(self.l_s, self.l_t)
		for i in range(1, self.l_s):
			self.h1s[i] = (self.x * self.h1s[i - 1] + ord(s[i - 1])) % self.m1
			self.h2s[i] = (self.x * self.h2s[i - 1] + ord(s[i - 1])) % self.m2
		for i in range(1, self.l_t):
			self.h1t[i] = (self.x * self.h1t[i - 1] + ord(t[i - 1])) % self.m1
			self.h2t[i] = (self.x * self.h2t[i - 1] + ord(t[i - 1])) % self.m2
		for i in range(1, min(self.l_s, self.l_t)):
			self.xl1[i] = (self.x * self.xl1[i - 1]) % self.m1
			self.xl2[i] = (self.x * self.xl2[i - 1]) % self.m2


	def solve(self):
		# 𝐻(𝑠𝑎𝑠𝑎+1 · · · 𝑠𝑎+𝑙−1) = ℎ[𝑎 + 𝑙] − 𝑥𝑙ℎ[𝑎]
		if debug:
			print('h1s', self.h1s, sep=', ')
			print('h1t', self.h1t, sep=', ')
		for l in reversed(range(1, min(self.l_s, self.l_t))):
		# tries = []
		# for l in range(1, min(self.l_s, self.l_t)):
			s_sub1, s_sub2 = [], []
			t_sub1, t_sub2 = [], []
			i_s = self.l_s
			i_t = self.l_t
			if debug:
				print('l ', l, sep=', ')
				print('l_s', self.l_s, sep=', ')
				print('l_t', self.l_t, sep=', ')
			i = 0
			while i + l < self.l_s:
				s_h1 = (self.h1s[i + l] - self.xl1[l] * self.h1s[i]) % self.m1
				s_h2 = (self.h2s[i + l] - self.xl2[l] * self.h2s[i]) % self.m2
				s_sub1.append(s_h1)
				s_sub2.append(s_h2)
				i += 1
			i = 0
			while i + l < self.l_t:
				t_h1 = (self.h1t[i + l] - self.xl1[l] * self.h1t[i]) % self.m1
				t_h2 = (self.h2t[i + l] - self.xl2[l] * self.h2t[i]) % self.m2
				t_sub1.append(t_h1)
				t_sub2.append(t_h2)
				i += 1
			for i_s in range(len(s_sub1)):
				for i_t in range(len(t_sub1)):
					if (s_sub1[i_s] == t_sub1[i_t]) and (s_sub2[i_s] == t_sub2[i_t]):
						return Answer(i_s, i_t, l)

		# find substrings that match of length 1, then test same positions with larger substrings
		return Answer(0, 0, 0)

'''
Naive implementation
def solve(s, t):
	# solving this problem in linear time
	# 𝑂(|𝑠| + |𝑡|). In this problem, your goal is to use hashing to solve it in almost linear time.
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans
'''

for line in sys.stdin.readlines():
	s, t = line.split()
	solver = Solver(s, t)
	ans = solver.solve()
	print(ans.i, ans.j, ans.len)
