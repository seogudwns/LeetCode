# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        lookup=set()
        while start:
            if start in lookup: return start
            else:
                lookup.add(start)
                start=start.next
        return None