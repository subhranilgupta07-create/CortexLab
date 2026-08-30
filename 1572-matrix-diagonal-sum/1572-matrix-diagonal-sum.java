class Solution 
{
    public int diagonalSum(int[][] mat) 
    {
        int a = 0, b = 0;
        for (int i = 0; i < mat.length; i++)
        {
            for (int j = 0; j < mat.length; j++)
            {
                if (i == j)
                {
                    a += mat[i][j];
                }
                else if ((i + j == mat.length - 1) && (i != j))
                {
                    b += mat[i][j];
                }
            }
        }
        return (a + b);
    }
}