# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = []
        curr = head
        while curr:
            heapq.heappush(x,curr.val)
            curr = curr.next
        
        curr = head
        while x:
            curr.val = heapq.heappop(x)
            curr = curr.next
        
        return head