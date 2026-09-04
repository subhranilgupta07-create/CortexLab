class Solution(object):
    def firstStableIndex(self, nums, k):
        c = 0
        for i in range (0, len(nums)):
            M = max(nums[0:i+1])
            m = min(nums[i:len(nums)])
            x = M - m
            if (x <= k):
                c = 1
                return i
        if (c == 0):
            return -1        