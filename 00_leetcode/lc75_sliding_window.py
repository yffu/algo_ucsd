from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 00643
        i, l, tot, tot_m = 0, len(nums), 0, 0
        while i < k:
            tot += nums[i]
            tot_m = tot
            i += 1
            # print("total: {}, total_max: {}".format(tot, tot_m))
        while i < l:
            tot += (nums[i] - nums[i - k])
            tot_m = max(tot_m, tot)
            i += 1
            # print("total: {}, total_max: {}".format(tot, tot_m))
        return tot_m / k

    def maxVowels(self, s: str, k: int) -> int:
        i, vcnt, vcnt_m, l = 0, 0, 0, len(s)
        while i < k:
            if s[i] in "aeiou":
                vcnt += 1
            i += 1
        vcnt_m = vcnt
        while i < l:
            if s[i] in "aeiou":
                vcnt += 1
            if s[i - k] in "aeiou":
                vcnt -= 1
            if vcnt > vcnt_m:
                vcnt_m = vcnt
            i += 1
        return vcnt_m

    def longestOnes(self, nums: List[int], k: int) -> int:
        i_0, i_1, f, cons_m, l = 0, 0, 0, 0, len(nums)
        while i_1 < l:
            if nums[i_1]:
                i_1 += 1
            elif not nums[i_1] and f < k:
                i_1 += 1
                f += 1
            elif not nums[i_1] and f >= k:
                if nums[i_0]:
                    i_0 += 1
                else:
                    i_0 += 1
                    i_1 += 1
            if i_1 - i_0 > cons_m:
                cons_m = i_1 - i_0
            # print("nums: {}, i_0: {}, i_1: {}, f: {}, k: {}, cons_m: {}".format(nums, i_0, i_1, f, k, cons_m))
        return cons_m

    def longestSubarray(self, nums: List[int]) -> int:
        i_0, i_1, dlt, cons_m, l = 0, 0, 1, 0, len(nums)
        while i_1 < l:
            if nums[i_1]:
                i_1 += 1
            else:
                if dlt:
                    i_1 += 1
                    dlt -= 1
                else:
                    # no dlt, and num[i_1] is 0
                    if nums[i_0]:
                        i_0 += 1
                    else:
                        i_0 += 1
                        dlt += 1
            if i_1 - i_0 - dlt > cons_m:
                # if dlt used, length reduced by 1
                # if dlt not used, length still reduced by 1
                cons_m = i_1 - i_0 - 1
            # print("nums: {}, i_0: {}, i_1: {}, dlt: {}, cons_m: {}".format(nums, i_0, i_1, dlt, cons_m))
        return cons_m


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(s.findMaxAverage([5], 1))
    print(s.maxVowels("abciiidef", 3))
    print(s.maxVowels("aeiou", 2))
    print(s.maxVowels("leetcode", 3))
    print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    print(s.longestSubarray([1, 1, 0, 1]))
    print(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print(s.longestSubarray([1, 1, 1]))
