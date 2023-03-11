# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        x = []
        while head:
            x.append(head.val)
            head = head.next
        
        def y(l,r):
            if l==r: return None
            mid = (l+r)//2
            node = TreeNode(val=x[mid])
            node.left = y(l,mid)
            node.right = y(mid+1,r)
            return node
        
        return y(0,len(x))