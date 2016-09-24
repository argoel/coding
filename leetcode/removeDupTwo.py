class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        prev = nums[0]
        count = 1
        i = 1
        while (i < len(nums)):
            cur = nums[i]
            if cur == prev:
                if count == 2:
                    nums.pop(i)
                else:
                    count += 1
                    i += 1
            else:
                i += 1
                prev = cur
                count = 1
        print nums
        return len(nums)

    def testRemoveDeuplicates(self):
        nums = [1,1,1,2,2,3]
        print self.removeDuplicates(nums)
        nums = [1,2,2,2]
        print self.removeDuplicates(nums)
