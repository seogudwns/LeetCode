# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        num = 0
        while current:
            current = current.next
            num += 1
        
        if num == n:
            return head.next
        # print(num)
        
        current = head
        while num != 1:
            if num == n+1:
                current.next = None or current.next.next
                break
            num -= 1
            current = current.next
            
        return head