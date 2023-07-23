# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n%2: return []

        dp=[[] for _ in range(n+1)]
        dp[1]=[TreeNode(0)]

        for i in range(3,n+1):
            for j in range(1,i):
                lt=dp[j]
                rt=dp[i-1-j]

                for leftSubtree in lt:
                    for rightSubtree in rt:
                        root=TreeNode()
                        root.left=leftSubtree
                        root.right=rightSubtree
                        dp[i].append(root)

        return dp[n]     