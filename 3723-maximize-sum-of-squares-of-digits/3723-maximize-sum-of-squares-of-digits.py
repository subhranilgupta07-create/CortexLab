class Solution(object):
    def maxSumOfSquares(self, num, sum):
        A = []
        for i in range(num):
            j = min(9, sum)
            A.append(str(j))
            sum -= j
        if sum > 0:
            return ""
        return ''.join(A)