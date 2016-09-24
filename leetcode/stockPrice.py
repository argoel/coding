class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minv = sys.maxint
        maxv = 0

        for i in range(len(prices)):
            minv = min(minv, prices[i])
            maxv = max(maxv, prices[i] - minv)

        return maxv
