class Solution(object):
    def hammingWeight(self, n):
        c = 0
        for i in range(32):
            a = 1 << i
            if n & a:
                c += 1
        return c