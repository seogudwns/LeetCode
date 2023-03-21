class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def fact(n): return n*(n+1)//2
        
        ans,tmp = 0,0
        
        for i in nums:
            if i == 0: tmp+=1
            else:
                ans+=fact(tmp)
                tmp = 0
        
        return ans+fact(tmp)