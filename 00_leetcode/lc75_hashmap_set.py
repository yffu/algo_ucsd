from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s_1, s_2 = {n for n in nums1}, {n for n in nums2}
        return [[n for n in s_1 if n not in s_2], [n for n in s_2 if n not in s_1]]

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        i, d, l = 0, dict(), len(arr)
        while i < l:
            if d.get(arr[i]):
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
            i += 1
        s = set()
        for n in d.values():
            if n in s:
                return False
            else:
                s.add(n)
        return True

    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = dict(), dict()
        for c in word1:
            if d1.get(c):
                d1[c] += 1
            else:
                d1[c] = 1
        for c in word2:
            if d2.get(c):
                d2[c] += 1
            else:
                d2[c] = 1

        d1_k = {k for k in d1.keys()}
        d2_k = {k for k in d2.keys()}
        d1_v = [v for v in d1.values()]
        d2_v = [v for v in d2.values()]
        d1_v.sort()
        d2_v.sort()
        # print("d1 keys: {}, d2 keys: {}".format(d1_k, d2_k))
        # print("d1 vals: {}, d2 vals: {}".format(d1_v, d2_v))
        return d1_k == d2_k and d1_v == d2_v

    def equalPairs(self, grid: List[List[int]]) -> int:
        j, l, d_c, cnt = 0, len(grid), dict(), 0
        while j < l:
            i, col = 0, list()
            while i < l:
                col.append(grid[i][j])
                i += 1
            col = tuple(col)
            if d_c.get(col):
                d_c[col] += 1
            else:
                d_c[col] = 1
            j += 1
        for r in grid:
            n = d_c.get(tuple(r))
            if n:
                cnt += n
        # print("d_c: {}".format(d_c))
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.findDifference([1, 2, 3], [2, 4, 6]))
    print(s.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
    print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(s.uniqueOccurrences([1, 2]))
    print(s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
    print(s.closeStrings("abc", "bca"))
    print(s.closeStrings("a", "aa"))
    print(s.closeStrings("cabbba", "abbccc"))
    print(s.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
    print(s.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
