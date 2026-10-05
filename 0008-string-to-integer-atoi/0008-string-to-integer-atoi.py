import re
class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        a = re.search(r"^[-+]?\d+", s)
        if not a:
            return 0
        x = a.group()
        sign = 1
        if x[0] == '-':
            sign = -1
            x = x[1:]
        elif x[0] == '+':
            x = x[1:]
        ans = 0
        for i in x:
            ans = ans * 10 + (ord(i) - ord('0'))
        ans = sign * ans
        if ans < -2147483648:
            return -2147483648
        if ans > 2147483647:
            return 2147483647
        return ans