class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.evaluatePaths(triangle)[0]

    def evaluatePaths(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype List[int] - best evaluated paths for every entry
        """
        if not triangle:
            return []

        topList = triangle[0]
        triangle.pop(0)
        if not triangle:
            return topList

        bottomList = self.evaluatePaths(triangle)

        #unnecessary check
        if len(bottomList) != len(topList) + 1:
            print "Some formatting error in data"
            return
        bestPathSum = [None]*len(topList)
        for i in range(len(topList)):
            val = topList[i]
            bP = min(val + bottomList[i], val + bottomList[i+1])
            bestPathSum[i] = bP
        return bestPathSum
