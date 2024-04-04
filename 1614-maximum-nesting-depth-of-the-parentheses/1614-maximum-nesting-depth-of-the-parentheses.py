class Solution:
    def maxDepth(self, s: str) -> int:
        ans,curr = 0,0
        for i in s:
            if i == "(":
                curr += 1
                ans = max(curr,ans)
            elif i == ")":
                curr -= 1
        
        return ans