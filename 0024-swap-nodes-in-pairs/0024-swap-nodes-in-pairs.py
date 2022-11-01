# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        n = 1
        while curr.next:
                
            if n%2:
                curr.val, curr.next.val = curr.next.val, curr.val
            
            n+= 1
            curr = curr.next
        
        return head