# python3

import sys
from collections import namedtuple
from random import randint

Answer = namedtuple('answer_type', 'i j len')
debug = True


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
		self.m1 = 1000000007
		self.x = randint(1, self.m1-1)
		'''
		self.xl1 = [1] * (self.l_s + 1)
		for i in range(1, self.l_s + 1):
			self.xl1[i] = (self.x * self.xl1[i - 1]) % self.m1
		print('xl1: ', self.xl1, sep=', ') if debug else None
		'''

		'''
		Implementation 1: Fails TC 7 going from largest l to smallest. Fails TC 5 going from smallest l to largest
		self.s = s
		self.t = t
		self.m1 = 1000000007
		self.m2 = 1000000009
		self.x = randint(1, self.m1-1)
		self.l_s, self.l_t = len(s)+1, len(t)+1
		self.h1s, self.h2s = [0] * self.l_s, [0] * self.l_s
		self.h1t, self.h2t = [0] * self.l_t, [0] * self.l_t
		self.xl1, self.xl2 = [1] * max(self.l_s, self.l_t), [1] * max(self.l_s, self.l_t)
		# how to optimize?
		for i in range(1, self.l_s):
			self.h1s[i] = (self.x * self.h1s[i - 1] + ord(s[i - 1])) % self.m1
			self.h2s[i] = (self.x * self.h2s[i - 1] + ord(s[i - 1])) % self.m2
		for i in range(1, self.l_t):
			self.h1t[i] = (self.x * self.h1t[i - 1] + ord(t[i - 1])) % self.m1
			self.h2t[i] = (self.x * self.h2t[i - 1] + ord(t[i - 1])) % self.m2
		for i in range(1, min(self.l_s, self.l_t)):
			self.xl1[i] = (self.x * self.xl1[i - 1]) % self.m1
			self.xl2[i] = (self.x * self.xl2[i - 1]) % self.m2
			'''


	def polyhash(self, str, m):
		answer = 0
		for c in reversed(str):
			answer = (answer * self.x + ord(c)) % m
		return answer

	def solve(self):
		for l in range(1, self.l_s + 1):
			answer_prev = Answer(0, 0, 0)
			answer = self.solve_l(l)
			if answer:
				answer_prev = answer
				continue
			else:
				return answer_prev
		return answer
		'''
		large to small
		for l in reversed(range(1, self.l_s + 1)):
			print('l: ', l, sep=',') if debug else None
			answer = self.solve_l(l)
			if answer:
				return answer
		return Answer(0, 0, 0)
		'''

	def solve_l(self, l):
		# 𝐻(𝑠𝑎𝑠𝑎+1 · · · 𝑠𝑎+𝑙−1) = ℎ[𝑎 + 𝑙] − 𝑥𝑙ℎ[𝑎]
		h_t = [0] * (self.l_t - l + 1)
		sub_t = self.t[self.l_t - l:]
		print('sub_t: ', sub_t, sep=', ') if debug else None
		h_t[self.l_t - l] = self.polyhash(sub_t, self.m1)
		y = 1
		for i in range(l):
			y = (y * self.x) % self.m1
		# y = self.xl1[l]
		print('y: ', y, sep=', ') if debug else None
		for i in reversed(range(0, self.l_t - l)):
			print('i: ', i, sep=', ') if debug else None
			h_t[i] = (self.x * h_t[i + 1] + ord(self.t[i]) - y * ord(self.t[i + l])) % self.m1
		print('h_t: ', h_t, sep=', ') if debug else None
		# convert h to dictionary of value : index
		d_t = {h_t[i]: i for i in range(len(h_t))}
		print('d_t: ', d_t, sep=', ') if debug else None

		h_s = [0] * (self.l_s - l + 1)
		sub_s = self.s[self.l_s - l:]
		print('sub_s: ', sub_s, sep=', ') if debug else None
		h_si = self.polyhash(sub_s, self.m1)
		h_s[self.l_s - l] = h_si if debug else None
		print('h_s: ', h_s, sep=', ') if debug else None
		if h_si in d_t:
			return Answer(d_t[h_si] if self.rev else self.l_s - l, self.l_s - l if self.rev else d_t[h_si], l)
		for i in reversed(range(0, self.l_s - l)):
			h_si = (self.x * h_si + ord(self.s[i]) - y * ord(self.s[i + l])) % self.m1
			h_s[i] = h_si if debug else None
			if h_si in d_t:
				print('found! ') if debug else None
				print('t_i: ', d_t[h_si], ' s_i: ', i, 'l: ', l, sep=', ') if debug else None
				return Answer(d_t[h_si] if self.rev else i, i if self.rev else d_t[h_si], l)
		print('h_s: ', h_s, sep=', ') if debug else None
		return None
		'''
		Implementation 1: Too slow
		found = [Answer(0,0,0)]
		if debug:
			print('h1s', self.h1s, sep=', ')
			print('h1t', self.h1t, sep=', ')
		for l in range(1, min(self.l_s, self.l_t)):
			s_sub1, s_sub2 = [], []
			t_sub1, t_sub2 = [], []
			i_s = self.l_s
			i_t = self.l_t
			if debug:
				print('l ', l, sep=', ')
				print('l_s', self.l_s, sep=', ')
				print('l_t', self.l_t, sep=', ')
			i = 0
			# implement a rolling hash function
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
						found.append(Answer(i_s, i_t, l))
			if debug:
				print('s_sub1', s_sub1, sep=', ')
				print('t_sub1', t_sub1, sep=', ')
				print('found ', found, sep=', ')
			if found[-1].len < l:
				break
		return found[-1]
		'''


for line in sys.stdin.readlines():
	s, t = line.split()
	solver = Solver(s, t)
	ans = solver.solve()
	print(ans.i, ans.j, ans.len)
