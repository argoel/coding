class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        added = 0
        i = 0
        while (miss <= n):
            if (i < len(nums) and miss >= nums[i]):
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added
