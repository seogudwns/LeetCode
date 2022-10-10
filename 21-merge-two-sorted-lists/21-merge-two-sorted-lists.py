# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # print(list1)
        # print(list2)
        result = ListNode(val=-101)
        current = result
        while list1 and list2:
            if list1.val<list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
        
        while list1:
            current.next = ListNode(val=list1.val)
            list1 = list1.next
            current = current.next
        
        while list2:
            current.next = ListNode(val=list2.val)
            list2 = list2.next
            current = current.next
            
        return result.next