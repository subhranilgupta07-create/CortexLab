class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        i = 2
        factors = []
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1
        if n > 1:
            factors.append(n)
        return all(x in [2, 3, 5] for x in factors)