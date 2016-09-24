class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        low, numDigSeen, digSize = self.findTenRange(n)
        #now n is between low and low*10

        cur = low
        curDig = numDigSeen

        diff = n - numDigSeen
        curPow = 10**digSize

        if diff == 0:
            #spit out first digit of curr
            return cur/(curPow/10)
        elif diff < digSize:
            #spit out relevant digit of curr
        else:
            while (n > curDig):



    def findTenRange(self, n):
        low = 1
        high = 9

        numDigSeen = 0
        numDigToBeSeen = 0
        digSize = 1

        while (n > numDigToBeSeen):
            numDigSeen = numDigToBeSeen
            numDigToBeSeen += (high - low + 1)*digSize
            low = high + 1
            high = high*10 + 9
            digSize += 1

        return low/10, numDigSeen, digSize-1
