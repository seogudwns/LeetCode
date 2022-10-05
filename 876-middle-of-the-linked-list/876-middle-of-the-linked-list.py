# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = head
        leng = 0
        while check:
            check = check.next
            leng += 1

        check = head
        leng //= 2
        while leng:
            check = check.next
            leng -= 1
        
        return check