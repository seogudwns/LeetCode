class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        ans,seen,k = [],deque(),0
        for i in nums:
            if i == -1:
                if k+1>len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k])
                k+=1
            else:
                k=0
                seen.appendleft(i)
                
        return ans