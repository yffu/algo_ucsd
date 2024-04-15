# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  result = []
  suffix = dict()
  for i in range(len(text)):
      suffix[text[i:]] = i
  suf_key = list(suffix.keys())
  suf_key.sort()
  for s in suf_key:
      result.append(suffix[s])
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
