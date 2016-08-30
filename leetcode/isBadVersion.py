# The isBadVersion API is already defined for ou.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        firstBadFound = False
        firstBadVersionNo = -1

        while(not(firstBadFound)):
            if high == low:
                firstBadFound = True
                firstBadersionNo = low

            mid = (low+high)/2
            midIsBad = isBadVersion(mid)

            if midIsBad:
                high = mid
            else:
                low = mid + 1

        return firstBadVersionNo
