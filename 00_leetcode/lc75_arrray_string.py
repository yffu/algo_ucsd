from typing import List
import sys


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 000238
        i, l = 1, len(nums)
        prod_pre = [1] * l
        prod_suf = [1] * l
        answer = []
        while i < l:
            prod_pre[i] = prod_pre[i - 1] * nums[i - 1]
            prod_suf[l - (i + 1)] = prod_suf[l - i] * nums[l - i]
            i += 1
        i = 0
        while i < l:
            answer.append(prod_pre[i] * prod_suf[i])
            i += 1
        return answer

    def increasingTriplet(self, nums: List[int]) -> bool:
        # 000334
        i, l = 0, len(nums)
        n_i, n_j = sys.maxsize, sys.maxsize
        while i < l:
            if nums[i] < n_i:
                n_i = nums[i]
                j = i + 1
                while j < l:
                    if n_j > nums[j] > n_i:
                        n_j = nums[j]
                        k = j + 1
                        while k < l:
                            if nums[k] > n_j:
                                return True, [nums[i], nums[j], nums[k]]
                            k += 1
                    j += 1
            i += 1
        return False

    def compress(self, chars: List[str]) -> int:
        i, j_0, j_1, l = 0, 0, 0, len(chars)
        while j_1 < l:
            print("chars: {}, i: {}, j_0: {}, j_1: {}, chars[j_0]: {}, chars[j_1]: {}".format(chars, i, j_0, j_1, chars[j_0], chars[j_1]))
            if chars[j_0] != chars[j_1]:
                i = j_0
                # write chars
                # set new j_0, j_1
                if j_1 - j_0 > 1:
                    chars[i] = chars[j_0]
                    i += 1
                    for c in str(j_1 - j_0):
                        chars[i] = c
                        i += 1
                j_0 = j_1
            j_1 += 1
        # i = 5, j = 7 == l
        if j_1 - j_0 > 1:
            chars[i] = chars[j_0]
            i += 1
            for c in str(j_1 - j_0):
                chars[i] = c
                i += 1
        print("chars: {}, i: {}, j_0: {}, j_1: {}".format(chars, i, j_0, j_1))
        l_n = i
        while i < l:
            chars.pop()
            i += 1
        print("chars: {}, i: {}, j_0: {}, j_1: {}".format(chars, i, j_0, j_1))
        return l_n


    def compress1(self, chars: List[str]) -> int:
        i, j, l = 0, 1, len(chars)
        while j < l:
            # len(chars)-1 for the last value of j
            if chars[j] != chars[j - 1]:
                chars[i] = chars[j - 1]
                c_l = j - i
                if c_l > 1:
                    for c in str(c_l):
                        i += 1
                        chars[i] = c
                i += 1
            j += 1
        print("i: {}, j: {}".format(i, j))
        c_l = j - i
        if c_l > 1:
            for c in str(c_l):
                i += 1
                chars[i] = c
        i += 1
        l_n = i
        while i < l:
            chars.pop()
            i += 1
        print("chars: {}".format(chars))
        return l_n


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print(s.increasingTriplet([1, 2, 3, 4, 5]))
    print(s.increasingTriplet([5, 4, 3, 2, 1]))
    print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(s.increasingTriplet([1, 2]))
    # Time Limit Exceeded
    # 32 / 84 testcases passed
    # Time Limit Exceeded
    # 76 / 84 testcases passed
    print(s.compress(["a", "a", "a", "b", "b", "a", "a"]))
    print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(s.compress(["a"]))
    print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
