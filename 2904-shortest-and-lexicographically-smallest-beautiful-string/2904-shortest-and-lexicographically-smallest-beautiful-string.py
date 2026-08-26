class Solution:
    def shortestBeautifulSubstring(self, s, k):
        p = 0
        c = 0
        start = 0
        A = [None] * len(s)
        for i in range(len(s)):
            if s[i] == '1':
                c += 1
            if c == k:
                while s[start] == '0':
                    start += 1
                A[p] = s[start:i + 1]
                p += 1
                c -= 1
                start += 1
        for i in range(p):
            for j in range(p - i - 1):
                if (len(A[j]) > len(A[j + 1]) or
                    (len(A[j]) == len(A[j + 1]) and
                     A[j] > A[j + 1])):
                    temp = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = temp
        if p == 0:
            return ""
        return A[0]