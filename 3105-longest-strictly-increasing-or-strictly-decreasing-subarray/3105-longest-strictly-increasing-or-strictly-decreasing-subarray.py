class Solution(object):
    def longestMonotonicSubarray(self, nums):
        c = 0
        A = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                c += 1
            else:
                A.append(c + 1)
                c = 0
        A.append(c + 1)
        c2 = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                c2 += 1
            else:
                A.append(c2 + 1)
                c2 = 0
        A.append(c2 + 1)
        return max(A)