class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        rstrs = []

        sortedStrDict = {}

        for st in strs:
            sortedStr = ''.join(sorted(st))
            if sortedStr in sortedStrDict:
                sortedStrDict[sortedStr].append(st)
            else:
                sortedStrDict[sortedStr] = [st]

        for key,val in sortedStrDict.iteritems():
            rstrs.append(val)

        return rstrs
