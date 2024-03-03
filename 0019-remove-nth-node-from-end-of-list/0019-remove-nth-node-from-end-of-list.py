# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        curr = head
        while curr:
            curr = curr.next
            leng+=1
        
        if leng == n: return head.next
        leng -= n
        curr = head
        while leng != 1:
            leng -= 1
            curr = curr.next
        curr.next = curr.next.next if curr.next.next else None
        
        return head