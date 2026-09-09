/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution 
{
    public int getDecimalValue(ListNode head) 
    {
        ListNode currNode = head;
        int S = 0;
        while (currNode != null)
        {
            S = 2 * S + currNode.val;
            currNode = currNode.next;
        }
        return S;
    }
}