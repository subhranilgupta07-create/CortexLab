class Solution(object):
    def resultArray(self, nums, k):
        C = [0] * k
        dp = [0] * k
        for num in nums:
            newDP = [0] * k
            m = num % k
            newDP[m] += 1
            for r in range(k):
                newDP[(r * m) % k] += dp[r]
            for r in range(k):
                C[r] += newDP[r]
            dp = newDP
        return C