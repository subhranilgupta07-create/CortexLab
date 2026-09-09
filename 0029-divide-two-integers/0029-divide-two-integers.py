class Solution(object):
    def divide(self, dividend, divisor):
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        c = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= temp + temp:
                temp += temp
                multiple += multiple
            dividend -= temp
            c += multiple
        if negative:
            c = -c
        if c > 2**31 - 1:
            return 2**31 - 1
        if c < -2**31:
            return -2**31
        return c