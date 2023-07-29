class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits = sorted(usageLimits)
    
        total, count = 0, 0
        for i in usageLimits:
            total += i
            if total >= ((count+1)*(count+2))//2:
                count += 1
                
        return count