# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        #
        prev = None
        cur = head
        
        while cur:
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = self.reverseList(slow.next)

        slow = slow.next

        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True

# TC - O(n)
# SC - O(1)
