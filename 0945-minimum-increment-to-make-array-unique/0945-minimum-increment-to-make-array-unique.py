class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        chk = [0 for _ in range(max(max(nums),len(nums))*2)]
        for i in nums: chk[i]+=1
        
        ans = 0
        for i in range(max(max(nums),len(nums))*2):
            if chk[i]>1:
                ans += chk[i]-1
                chk[i+1]+=chk[i]-1
        
        return ans