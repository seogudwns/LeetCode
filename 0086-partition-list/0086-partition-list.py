# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        low,high = [],[]
        curr = head
        while curr:
            if curr.val < x:
                low.append(curr.val)
            else:
                high.append(curr.val)
            
            curr = curr.next
        
        curr = head
        for i in low+high:
            curr.val = i
            curr = curr.next
        
        return head