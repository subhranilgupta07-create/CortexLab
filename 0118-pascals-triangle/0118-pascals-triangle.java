class Solution 
{
    public List<List<Integer>> generate(int numRows) 
    {
        List<List<Integer>> A = new ArrayList<>();
        for (int i = 0; i < numRows; i++) 
        {
            List<Integer> B = new ArrayList<>();
            for (int j = 0; j < i + 1; j++) 
            {
                if (j == 0 || j == i) 
                {
                    B.add(1);
                } 
                else 
                {
                    B.add(A.get(i - 1).get(j - 1) + A.get(i - 1).get(j));
                }
            }
            A.add(B);
        }
        return A;
    }
}