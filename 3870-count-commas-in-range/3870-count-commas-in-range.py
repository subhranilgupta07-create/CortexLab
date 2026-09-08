class Solution(object):
    def countCommas(self, n):
        y = 0
        for i in range (1000, n + 1):
            x = i
            c = 0
            while (x > 0):
                x //= 10
                c += 1
            y += ((c - 1) // 3)         
        return y       