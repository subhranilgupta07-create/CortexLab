class Solution 
{
    public boolean isHappy(int n) 
    {
        int x = n;
        while (x != 1 && x != 4)
        {
            int S = 0;
            for (int i = x; i > 0; i /= 10)
            {
                int j = i % 10;
                S += (int)Math.pow(j, 2);
            }
            x = S;
        }
        return (x == 1);
    }
}