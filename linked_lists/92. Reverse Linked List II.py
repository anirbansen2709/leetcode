# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        lp = head
        left_prev = None
        for _ in range(left-1):
            left_prev = lp
            lp = lp.next
        
        prev = None
        cur = lp
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

        left_prev.next.next = cur
        left_prev.next = prev
        
        return head
