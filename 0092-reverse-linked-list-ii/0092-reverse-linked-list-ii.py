# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        lN = head
        l = 1
        while lN:
            if l == left: break
            lN = lN.next
            l+=1

        right -= left-1
        rN = lN
        tmp = []
        while right:
            tmp.append(rN.val)
            rN = rN.next
            right -= 1
        
        while tmp:
            lN.val = tmp.pop()
            lN = lN.next
            
        return head