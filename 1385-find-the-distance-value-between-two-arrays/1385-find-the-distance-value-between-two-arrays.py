class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        c = 0
        y = 0
        for i in range (len(arr1)):
            for j in range (len(arr2)):
                x = abs(arr1[i] - arr2[j])
                if (x > d):
                    c += 1
            if (c == len(arr2)):
                y += 1
            c = 0       
        return y    