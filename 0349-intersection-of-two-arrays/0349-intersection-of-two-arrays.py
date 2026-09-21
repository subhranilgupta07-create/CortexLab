class Solution(object):
    def intersection(self, nums1, nums2):
        A = list(set(nums1))
        B = list(set(nums2))
        C = []
        for i in range (len(A)):
            if (A[i] in B):
                C.append(A[i])
        return C        