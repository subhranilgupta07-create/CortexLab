class Solution(object):
    def hammingWeight(self, n):
        x = int(bin(n)[2:])
        c = 0
        while x > 0:
            j = x % 10
            if j == 1:
                c += 1
            x //= 10
        return c        