# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        x = deque()
        curr = head
        while curr:
            x.append(curr.val)
            curr = curr.next
        
        eo = 1
        curr = head
        while x:
            if eo%2:
                curr.val = x.popleft()
            else:
                curr.val = x.pop()
            curr = curr.next
            eo += 1
        
        return head