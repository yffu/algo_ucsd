from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 000283
        """
        Do not return anything, modify nums in-place instead.
        """
        i_0, i_1, l = 0, 0, len(nums)
        while i_1 < l:
            if nums[i_1]:
                nums[i_0] = nums[i_1]
                i_0 += 1
            i_1 += 1
        while i_0 < l:
            nums[i_0] = 0
            i_0 += 1

    def isSubsequence(self, s: str, t: str) -> bool:
        # 000392
        i_s, i_t, l_s, l_t = 0, 0, len(s), len(t)
        while i_s < l_s and i_t < l_t:
            if s[i_s] == t[i_t]:
                i_s += 1
            i_t += 1
        if i_s == l_s:
            return True
        else:
            return False

    def maxArea(self, height: List[int]) -> int:
        # 000011
        i_0, i_1, l = 0, 0, len(height)
        max_area = 0
        while i_0 < l - (i_1 + 1):
            max_area = max(max_area, (l - (i_0 + i_1 + 1)) * min(height[i_0], height[l - (i_1 + 1)]))
            if height[i_0] > height[l - (i_1 + 1)]:
                i_1 += 1
            else:
                i_0 += 1
        return max_area

    def maxOperations(self, nums: List[int], k: int) -> int:
        # 001679
        nums.sort()
        i_0, i_1, l = 0, 0, len(nums)
        ops = 0
        while i_0 < l - (i_1 + 1):
            s = nums[i_0] + nums[l - (i_1 + 1)]
            if s == k:
                ops += 1
                i_0 += 1
                i_1 += 1
            elif s < k:
                # sum is too small
                i_0 += 1
            else:
                # sum is too large
                i_1 += 1
        return ops


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)
    nums = [0]
    s.moveZeroes(nums)
    print(nums)
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea([1, 1]))
    print(s.maxOperations([1, 2, 3, 4], 5))
    print(s.maxOperations([3, 1, 3, 4, 3], 6))
