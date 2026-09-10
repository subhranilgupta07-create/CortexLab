class Solution(object):
    def digitFrequencyScore(self, n):
        S = 0
        while n > 0:
            S += (n % 10)
            n /= 10
        return S    