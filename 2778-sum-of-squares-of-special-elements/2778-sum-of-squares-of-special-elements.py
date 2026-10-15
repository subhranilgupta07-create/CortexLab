class Solution(object):
    def sumOfSquares(self, nums):
        x = 0
        for i in range (len(nums)):
            if (len(nums) % (i + 1) == 0):
                x += nums[i] ** 2
        return x        