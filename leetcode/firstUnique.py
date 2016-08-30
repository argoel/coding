class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        nonRepeats = {}
        repeats = {}
        firstUnique = -1
        for ch in s:
            if ch in nonRepeats:
                if ch in nonRepeats:
                    repeats[ch] = 1
                else:
                    nonRepeats[ch] = 1

            for i in range(len(s)):
                ch = s[i]
                if ch not in repeats:
                    firstUnique = i
                    break
        return firstUnique
