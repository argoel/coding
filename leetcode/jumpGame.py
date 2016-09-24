class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jumps = 0
        farthest = 0
        curfarthest = 0
        i = 0
        n = len(nums)

        while(i < n-1):
            curfarthest = max(curfarthest, i + nums[i])
            if (i == farthest):
                farthest = curfarthest
                jumps += 1
            i += 1
        return jumps
