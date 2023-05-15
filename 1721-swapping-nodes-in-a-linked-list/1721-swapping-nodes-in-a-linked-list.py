# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head=head.next
        tmp[k-1],tmp[-k] = tmp[-k],tmp[k-1]
        
        nex = ListNode(val=tmp.pop())
        while tmp:
            curr = ListNode(val=tmp.pop())
            curr.next = nex
            nex = curr
        
        return nex