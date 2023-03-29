class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction)
        curr,mask = 0,sum(satisfaction)
        
        for i in range(len(satisfaction)): curr += (i+1)*satisfaction[i]
        ans = curr
        
        for i in range(len(satisfaction)):
            curr -= mask
            mask -= satisfaction[i]
            ans = max(ans,curr)
            
        return ans