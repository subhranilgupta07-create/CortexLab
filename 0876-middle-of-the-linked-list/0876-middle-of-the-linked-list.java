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
    public ListNode middleNode(ListNode head) 
    {
        int size = 0;
        ListNode currNode = head;
        while (currNode != null)
        {
            currNode = currNode.next;
            size++;
        }
        int x = (size/2);
        currNode = head;
        int p = 0;
        while (p < x)
        {
            currNode = currNode.next;
            p++;
        }
        return currNode;
    }
}