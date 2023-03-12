# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        while lists:
            lst = lists.pop()
            while lst:
                heapq.heappush(vals,lst.val)
                lst = lst.next
        
        if not vals: return None
        
        ans = ListNode(val = heapq.heappop(vals))
        curr = ans
        while vals:
            curr.next = ListNode(val = heapq.heappop(vals))
            curr = curr.next
        
        return ans