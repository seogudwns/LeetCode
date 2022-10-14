# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        curr = head
        n = 0
        while curr:
            n+=1
            curr = curr.next
        
        n//=2
        
        curr = head
        while n != 1:
            curr = curr.next
            n -= 1
        
        curr.next = curr.next.next if curr.next.next else None
        
        return head