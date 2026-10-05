import re
class Solution(object):
    def areNumbersAscending(self, s):
        A = [int(x) for x in re.findall(r"\d+", s)]
        for i in range(len(A) - 1):
            if A[i] >= A[i + 1]:
                return False
        return True            