class Solution(object):
    def removeOuterParentheses(self, s):
        c = 0
        A = []
        j = 0
        for i in range (len(s)):
            if s[i] == '(':
                c += 1
            if s[i] == ')':
                c -= 1
            if (c == 0):
                A.append(s[j + 1: i])
                j = i + 1
        return ''.join(A)      