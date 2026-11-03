class Solution(object):
    def minMoves(self, nums):
        S = 0
        for i in range (len(nums)):
            S += max(nums) - nums[i]    
        return S       