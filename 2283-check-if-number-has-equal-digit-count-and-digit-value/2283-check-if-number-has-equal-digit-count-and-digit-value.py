import re
class Solution(object):
    def digitCount(self, num):
        for i in range(len(num)):
            if len(re.findall(str(i), num)) != int(num[i]):
                return False
        return True