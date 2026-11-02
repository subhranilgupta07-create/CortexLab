class Solution(object):
    def minMoves(self, nums):
        c = 0
        m = min(nums)
        for i in range(len(nums)):
            c += nums[i] - m
        return c