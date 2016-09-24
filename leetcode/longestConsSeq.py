from sets import Set

class Solution(object):
    def longestConsecutie(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = Set(nums)

        H = {}
        marked = {}

        for n in nums:
            if n in marked:
                continue
            mL = n-1
            while mL in nums:
                marked[mL] = 1
                mL -= 1
            mL += 1
            mH = n+1
            while mH in nums:
                marked[mH] = 1
                mH += 1
            mH -= 1
            H[mH] = mH - mL + 1

        maxv = 0
        for key, val in H.items():
            if val > maxv:
                maxv = val
        return maxv
