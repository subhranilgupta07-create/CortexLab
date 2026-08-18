class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A = []
        for i in nums1:
            A.append(i)
        for j in nums2:
            A.append(j)
        A.sort()
        p = len(A)
        if (len(A) % 2 == 0):
            return ((float)(A[len(A)/2]+ A[(len(A)/2)-1])/2)
        else:
            return (A[len(A)/2])       