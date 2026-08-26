class Solution {
    public String shortestBeautifulSubstring(String s, int k) 
    {
        int p = 0;
        int c = 0;
        int start = 0;
        String A[] = new String [s.length()];
        for (int i = 0; i < s.length(); i++)
        {
            if (s.charAt(i)=='1')
            {
                c++;
            }
            if (c == k)
            {
                while (s.charAt(start) == '0') 
                {
                    start++;
                }
                A[p] = s.substring(start, i+1);
                p++;
                c--;
                start++;
            }
        }
        for (int i = 0; i < p; i++)
        {
            for (int j = 0; j < p - i - 1; j++)
            {
                if (A[j].length() > A[j + 1].length() ||
                    (A[j].length() == A[j + 1].length() &&
                     A[j].compareTo(A[j + 1]) > 0)) 
                {
                    String temp = A[j];
                    A[j] = A[j + 1];
                    A[j + 1] = temp;
                }
            }
        }
        if (p == 0)
        {
            return "";
        }
        return (A[0]);
    }
}