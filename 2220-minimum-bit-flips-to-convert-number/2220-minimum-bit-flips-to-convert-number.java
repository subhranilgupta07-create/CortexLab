class Solution 
{
    public int minBitFlips(int start, int goal) 
    {
        String s1 = "";
        String s2 = "";
        for (int i = start; i > 0; i /= 2)
        {
            s1 += (i % 2);
        }
        for (int i = goal; i > 0; i /= 2)
        {
            s2 += (i % 2);
        }
        while (s1.length() < s2.length())
        {
            s1 += "0";
        }
        while (s2.length() < s1.length())
        {
            s2 += "0";
        }
        int c = 0;
        for (int i = 0; i < s1.length(); i++)
        {
            if (s1.charAt(i) != s2.charAt(i))
            {
                c++;
            }
        }
        return c;
    }
}