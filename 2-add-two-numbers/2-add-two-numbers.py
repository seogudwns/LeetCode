# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while l1:
            lst.append(str(l1.val))
            l1 = l1.next
        num1 = int(''.join(lst[::-1]))
        
        lst = []
        while l2:
            lst.append(str(l2.val))
            l2 = l2.next
        num2 = int(''.join(lst[::-1]))
        
        last = str(num1+num2)[::-1]
        result = ListNode(val = int(last[0]))
        current = result
        
        for i in range(1,len(last)):
            current.next = ListNode(val = int(last[i]))
            current = current.next
        
        return result