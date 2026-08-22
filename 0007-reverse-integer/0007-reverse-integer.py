class Solution(object):
    def reverse(self, x):
        a = str(x)
        b = a[::-1]
        if a[0] == '-':
            c = -int(b[0:len(a)-1])
        else:
            c = int(b)
        if c < -2**31 or c > 2**31 - 1:
            return 0
        return c