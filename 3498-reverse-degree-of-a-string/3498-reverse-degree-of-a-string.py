class Solution(object):
    def reverseDegree(self, s):
          S = 0
          for i in range (len(s)):
            a = 123 - ord(s[i])
            S += (a * (i + 1))
          return S  