# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        chk = set()
        curr = head
        while curr:
            chk.add(curr.val)
            while curr.next and curr.next.val in chk:
                if curr.next.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None
            curr = curr.next
        
        return head