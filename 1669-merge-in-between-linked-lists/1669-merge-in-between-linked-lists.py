# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        lst2last = list2
        while lst2last.next:
            lst2last = lst2last.next
        apart = list1
        for i in range(a-1):
            apart = apart.next
        
        bpart = apart
        for i in range(b-a+2):
            bpart = bpart.next
            
        lst2last.next = bpart
        apart.next = list2

        return list1