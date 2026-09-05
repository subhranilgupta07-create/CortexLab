class Solution:
    def isHappy(self, n):
        x = n
        while x != 1 and x != 4:
            S = 0
            i = x
            while i > 0:
                j = i % 10
                S += j ** 2
                i //= 10
            x = S
        return x == 1