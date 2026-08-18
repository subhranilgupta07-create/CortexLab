class Solution 
{
    public double findMedianSortedArrays(int[] nums1, int[] nums2) 
    {
        int m = nums1.length;
        int n = nums2.length;
        int A[] = new int [m + n];
        int c = 0;
        for (int i = 0; i < m; i++)
        {
            A[i] = nums1[i];
            c++;
        }
        for (int i = 0; i < n; i++)
        {
            A[c+i] = nums2[i];
        }
        Arrays.sort(A);
        int p = m + n;
        if (p % 2 == 0)
        {
            return (((double)(A[p/2]+ A[(p/2)-1])/2));
        }
        else
        {
            return (A[p/2]);
        }
    }
}