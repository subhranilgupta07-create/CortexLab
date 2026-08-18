class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A = []
        for i in nums1:
            A.append(i)
        for j in nums2:
            A.append(j)
        A.sort()
        p = len(A)
        if (p % 2 == 0):
            return ((float)(A[p/2]+ A[(p/2)-1])/2)
        else:
            return (A[p/2])       