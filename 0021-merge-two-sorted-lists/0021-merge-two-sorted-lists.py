class Solution(object):
    def mergeTwoLists(self, list1, list2):
        A = []

        while list1:
            A.append(list1.val)
            list1 = list1.next

        while list2:
            A.append(list2.val)
            list2 = list2.next

        A.sort()

        dummy = ListNode(0)
        current = dummy

        for x in A:
            current.next = ListNode(x)
            current = current.next

        return dummy.next