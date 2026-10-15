
class Solution(object):
    def maxSum(self, nums, k):
        def Square(A):
            S = 0
            for i in range(len(A)):
                S += A[i] ** 2
            return S
        count = [0] * 32
        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    count[b] += 1
        A = []
        for p in range(k):
            num = 0
            for b in range(32):
                if count[b] > 0:
                    num |= (1 << b)
                    count[b] -= 1
            A.append(num)
        return Square(A) % (10**9 + 7)
