# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        lower = 1
        higher = n
        found = False
        rightGuess = -1

        while not(found):
            mid = (higher + lower)/2
            g = guess(mid)
            if g == 0:
                found = True
                rightGuess = mid
            elif g == -1:
                higher = mid -1
            elif g == 1:
                lower = mid + 1

        return rightGuess
