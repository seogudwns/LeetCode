class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        ans,seen,k = [],deque(),0
        for i in nums:
            if i == -1:
                ans.append(-1 if k+1>len(seen) else seen[k])
                k+=1
            else:
                seen.appendleft(i)
                k=0
                
        return ans