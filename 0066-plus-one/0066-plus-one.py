class Solution(object):
    def plusOne(self, digits):
        a = ""
        for i in range (0, len(digits)):
            a += str(digits[i])
        b = str(int(a) + 1)
        A = []
        for i in range (0, len(b)):
            A.append(int(b[i]))
        return A    