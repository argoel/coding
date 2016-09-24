class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        count1, count2, cand1, cand2 = 0,0,0,1

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                count1, cand1 = 1, n
            elif count2 == 0:
                count2, cand2 = 1, n
            else:
                count1 -= 1
                count2 -= 1

        returnList = []
        if nums.count(cand1) > len(nums)/3:
            returnList.append(cand1)
        if nums.count(cand2) > len(nums)/3:
            returnList.append(cand2)
        return returnList

    def testMajorityElement(self):
        nums = [1,1,2,3,4,4,4,2,4,1,1,1,4,2,4,1]
        print len(nums)
        self.majorityElement(nums)
