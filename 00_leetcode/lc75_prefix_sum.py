from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        i, alt, alt_m, l = 0, 0, 0, len(gain)
        while i < l:
            alt += gain[i]
            if alt > alt_m:
                alt_m = alt
            # print("i: {}, alt: {}, alt_m: {}".format(i, alt, alt_m))
            i += 1
        return alt_m

    def pivotIndex(self, nums: List[int]) -> int:
        i_0, s_0, s_1, l = 0, 0, 0, len(nums)
        s_l, s_r = [0] * l, [0] * l
        while i_0 < l:
            s_l[i_0] = s_0
            s_r[l - (i_0 + 1)] = s_1
            s_0 += nums[i_0]
            s_1 += nums[l - (i_0 + 1)]
            i_0 += 1
        i_0 = 0
        # print("nums: {}".format(nums))
        # print("s_l: {}".format(s_l))
        # print("s_r: {}".format(s_r))
        while i_0 < l:
            if s_l[i_0] == s_r[i_0]:
                return i_0
            i_0 += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.largestAltitude([-5, 1, 5, 0, -7]))
    print(s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
    print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(s.pivotIndex([1, 2, 3]))
    print(s.pivotIndex([2, 1, -1]))
    print(s.pivotIndex([-1, -1, -1, -1, -1, 0]))
