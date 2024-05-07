# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0 and not head.next: return ListNode(val=0)
        num = 0
        while head:
            num = num*10 + head.val
            head = head.next
        num *= 2
        curr = False
        while num:
            x,y = divmod(num,10)
            if x:
                curr = ListNode(val=y,next=curr) if curr else ListNode(val=y)
                num = x
            else:
                return ListNode(val=y) if not curr else ListNode(val=y,next=curr)
            