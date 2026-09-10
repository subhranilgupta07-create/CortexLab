class Solution 
{
    public ListNode removeNthFromEnd(ListNode head, int n) 
    {
        int size = 0;
        ListNode currNode = head;
        while (currNode != null)
        {
            size++;
            currNode = currNode.next;
        }
        if (n == size)
        {
            return head.next;
        }
        currNode = head;
        for (int i = 0; i < size - n - 1; i++)
        {
            currNode = currNode.next;
        }
        currNode.next = currNode.next.next;
        return head;
    }
}