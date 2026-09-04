class Solution 
{
    public int firstStableIndex(int[] nums, int k) 
    {
        int c = 0;
        for (int i = 0; i < nums.length; i++) 
        {
            int M = nums[0];
            for (int j = 0; j <= i; j++) 
            {
                M = Math.max(M, nums[j]);
            }
            int m = nums[i];
            for (int j = i; j < nums.length; j++) 
            {
                m = Math.min(m, nums[j]);
            }
            int x = M - m;
            if (x <= k) 
            {
                c = 1;
                return i;
            }
        }
        if (c == 0) 
        {
            return -1;
        }
        return -1;
    }
}