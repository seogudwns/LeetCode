# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l2.val == 0: return ListNode(val=0)
        num1,num2 = 0,0
        while l1:
            num1+=l1.val
            l1= l1.next
            num1*=10
        while l2:
            num2+=l2.val
            l2 = l2.next
            num2*=10
        
        num = (num1+num2)//10
        
        nums = []
        while True:
            x,y = divmod(num,10)
            if not x and not y:
                break
            nums.append(y)
            num = x
        
        nums = nums[::-1]

        node = ListNode(val=nums[0])
        curr = node
        for i in range(1,len(nums)):
            curr.next = ListNode(val=nums[i])
            curr = curr.next
        
        return node
        
        
        
        