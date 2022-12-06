# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []
        odd = []
        n = 1
        o,e = 1,0
        
        while head:
            if n%2:
                odd.append(head.val)
            else:
                even.append(head.val)
            
            n += 1
            head = head.next
        
        res = ListNode()
        curr = res
        for i in odd+even:
            curr.next = ListNode(val = i)
            curr = curr.next
        
        return res.next