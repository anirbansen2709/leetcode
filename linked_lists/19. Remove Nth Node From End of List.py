# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next
        
        slow = head
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        next_node = slow.next
        prev.next = next_node
        return head

# TC - O(n)
# SC - O(1)
