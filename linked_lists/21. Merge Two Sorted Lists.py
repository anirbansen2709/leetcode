# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        cur = None
        while list1 and list2:
            if list1.val < list2.val:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            if cur:
                cur.next = ListNode(value)
                cur = cur.next
            else:
                new_head = ListNode(value)
                cur = new_head
        while list1:
            value = list1.val
            list1 = list1.next
            if cur:
                cur.next = ListNode(value)
                cur = cur.next
            else:
                new_head = ListNode(value)
                cur = new_head
        while list2:
            value = list2.val
            list2 = list2.next
            if cur:
                cur.next = ListNode(value)
                cur = cur.next
            else:
                new_head = ListNode(value)
                cur = new_head
        return new_head

# T - O(n + m)
# S - O(1)
