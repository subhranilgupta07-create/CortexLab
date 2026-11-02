class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums)//2]
        S = 0
        for i in range(len(nums)):
            S += abs(nums[i] - median)
        return S