# python3
import sys
debug = False


class Node:
	def __init__(self):
		self.next = list()
		self.symbol = list()

	def __str__(self):
		return "node with id: {} labels: {} and next: {}".format(hex(id(self)), self.symbol, self.next)

	def has_symbol(self, s):
		return s in self.symbol

	def get_next(self, s):
		return self.next[self.symbol.index(s)]

	def set_next(self, s, n):
		self.symbol.append(s)
		self.next.append(n)

	def is_leaf(self):
		return not self.next


def trie_construction(patterns):
	trie = Node()
	for pattern in patterns:
		current_node = trie
		for symbol in pattern:
			if current_node.has_symbol(symbol):
				current_node = current_node.get_next(symbol)
			else:
				new_node = Node()
				current_node.set_next(symbol, new_node)
				current_node = new_node
	return trie


def prefix_trie_matching(text, trie):
	pos = 0
	symbol = text[0]
	v = trie
	if debug: print("text: {}".format(text))
	while True:
		if debug: print("node: {} ".format(v))
		if v.is_leaf():
			return True
		elif v.has_symbol(symbol):
			v = v.get_next(symbol)
			pos += 1
			symbol = text[pos]
		else:
			return False


def trie_matching(text, trie, result):
	for i in range(len(text)):
		if prefix_trie_matching(text[i:], trie):
			result.append(i)


def solve(text, n, patterns):
	result = []

	# write your code here
	trie = trie_construction(patterns)
	if debug:
		print(trie)
		print(patterns)
	trie_matching(text+"$", trie, result)

	return result


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	n = int(sys.stdin.readline().strip())
	patterns = []
	for i in range(n):
		patterns += [sys.stdin.readline().strip()]

	ans = solve(text, n, patterns)

	sys.stdout.write(' '.join(map(str, ans)) + '\n')
