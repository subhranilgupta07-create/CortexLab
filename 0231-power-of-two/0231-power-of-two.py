class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        for i in range(32):
            if n >> i == 1:
                if n == (1 << i):
                    return True
        return False