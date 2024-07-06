# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        dummy = ListNode(-1, head)
        prev = dummy
        cur = head

        while cur and cur.next:

            next_node = cur.next
            next_pair = cur.next.next

            prev.next = next_node
            next_node.next = cur
            cur.next = next_pair
            
            prev = cur
            cur = next_pair

        return dummy.next      

# TC - O(n)
# SC - O(1)
