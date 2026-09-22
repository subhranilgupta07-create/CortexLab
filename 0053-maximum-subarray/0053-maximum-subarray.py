class Solution(object):
    def maxSubArray(self, nums):
        M = nums[0]
        S = 0
        for i in range(len(nums)):
            S += nums[i]
            if S > M:
                M = S
            if S < 0:
                S = 0
        return M