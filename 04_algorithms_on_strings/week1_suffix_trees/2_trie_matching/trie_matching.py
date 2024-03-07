# python3
import sys
debug = False


class TrieNode:
	def __init__(self):
		self.children = [None] * 26
		self.leaf = False


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word: str) -> None:
		current = self.root
		for letter in word:
			index = ord(letter) - ord('A')
			if not current.children[index]:
				current.children[index] = TrieNode()
			current = current.children[index]
		current.leaf = True

	def trie_construction(self, patterns) -> None:
		for pattern in patterns:
			self.insert(pattern)

	def prefix_trie_matching(self, word: str) -> None:
		if debug: print(word)
		current = self.root
		for id, letter in enumerate(word):
			index = ord(letter) - ord('A')
			# scenario where word and pattern match but word is longer, check if current trie node is leaf and return if so
			if current.leaf:
				return True
			if not current.children[index]:
				return False
			current = current.children[index]
		# scenario where word and pattern are same length, and we need to check if last trie node is leaf before last letter in word
		return current.leaf


def trie_matching(text, trie, result):
	for i in range(len(text)):
		if trie.prefix_trie_matching(text[i:]):
			result.append(i)


def solve(text, n, patterns):
	result = []

	# write your code here
	trie = Trie()
	trie.trie_construction(patterns)
	trie_matching(text, trie, result)

	return result


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	n = int(sys.stdin.readline().strip())
	patterns = []
	for i in range(n):
		patterns += [sys.stdin.readline().strip()]

	ans = solve(text, n, patterns)

	sys.stdout.write(' '.join(map(str, ans)) + '\n')

"""
https://wangyy395.medium.com/implement-a-trie-in-python-e8dd5c5fde3a
"""
