# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        chk = []
        while head:
            heapq.heappush(chk,head.val)
            head = head.next
        
        ans = ListNode(heapq.heappop(chk))

        nex = ans
        while chk:
            nex.next = ListNode(heapq.heappop(chk))
            nex = nex.next

        return ans