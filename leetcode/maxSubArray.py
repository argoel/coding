class Solution(object):
    def maxSubArrayLinear(self, nums):
        n = len(nums)
        maxSumEndingAt = [0]*n

        for i in range(n):
            if i == 0:
                maxSumEndingAt[i] = nums[i]
            else:
                maxSumEndingAt[i] = max(nums[i], maxSumEndingAt[i-1] + nums[i])

        maxSum = maxSumEndingAt[0]

        for sum in maxSumEndingAt:
            maxSum = max(maxSum, sum)

        return maxSum
