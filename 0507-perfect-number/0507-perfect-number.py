class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        S = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                S += i
                if i != num // i:
                    S += num // i
            i += 1
        return S == num