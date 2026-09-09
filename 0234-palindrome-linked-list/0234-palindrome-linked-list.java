import java.util.Arrays;
class Solution 
{
    public boolean isPalindrome(ListNode head) 
    {
        int size = 0;
        ListNode currNode = head;
        while (currNode != null)
        {
            currNode = currNode.next;
            size++;
        }
        int A[] = new int[size / 2];
        int B[] = new int[size / 2];
        currNode = head;
        for (int i = 0; i < size / 2; i++)
        {
            A[i] = currNode.val;
            currNode = currNode.next;
        }
        if (size % 2 != 0)
        {
            currNode = currNode.next;
        }
        for (int i = size / 2 - 1; i >= 0; i--)
        {
            B[i] = currNode.val;
            currNode = currNode.next;
        }
        return Arrays.equals(A, B);
    }
}