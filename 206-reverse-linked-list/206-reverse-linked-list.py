# setrecursionlimit(10**5)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def recurs(curr):
#             if not curr.next:
#                 return ListNode(val=curr.val)
            
#             X = recurs(curr.next)
#             X.next = curr
#             return X
        
#         return recurs(head) # ... 재귀로 풀어야 하는데 생각이 구찮다..
        if not head:
            return head
        
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        result = ListNode(val=lst[-1])
        current = result
        
        for i in lst[-2::-1]:
            current.next = ListNode(val=i)
            current=current.next
        
        return result
        

        