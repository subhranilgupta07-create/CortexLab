class Solution(object):
    def buildArray(self, nums):
        A = []
        for i in range (len(nums)):
            A.append(nums[nums[i]])        
        return A    