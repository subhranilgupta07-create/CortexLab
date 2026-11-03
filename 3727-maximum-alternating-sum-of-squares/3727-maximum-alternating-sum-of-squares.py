class Solution(object):
    def maxAlternatingSum(self, nums):
        A = sorted(x*x for x in nums)
        n = len(A)
        k = n // 2
        return sum(A[k:]) - sum(A[:k])