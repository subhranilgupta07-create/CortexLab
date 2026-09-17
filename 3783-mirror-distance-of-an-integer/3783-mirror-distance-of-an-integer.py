class Solution(object):
    def mirrorDistance(self, n):
        a = n
        b = int(str(a)[::-1])
        return (abs(a - b))