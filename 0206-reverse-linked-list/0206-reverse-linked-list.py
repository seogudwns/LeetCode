# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        result = ListNode(val=lst.pop())
        current = result
        
        while lst:
            current.next = ListNode(val=lst.pop())
            current=current.next
        
        return result
        