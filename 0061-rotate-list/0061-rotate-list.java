class Solution 
{
    public ListNode rotateRight(ListNode head, int k) 
    {
        if (head == null || head.next == null || k == 0)
        {
            return head;
        }
        int size = 1;
        ListNode temp = head;
        while (temp.next != null)
        {
            size++;
            temp = temp.next;
        }
        k = k % size;
        for (int i = 1; i <= k; i++) 
        {
            ListNode secondLast = head;
            ListNode LastNode = head.next;
            while (LastNode.next != null) 
            {
                secondLast = secondLast.next;
                LastNode = LastNode.next;
            }
            LastNode.next = head;
            secondLast.next = null;
            head = LastNode;
        }
        return head;
    }
}