class Solution:
#     # TLE.
#     @lru_cache(None)
#     def chk(self,curri):
#         num,ans = self.arr[curri],1
#         for i in range(curri):
#             for j in range(i+1):
#                 if num == self.arr[i]*self.arr[j]: ans = (ans+self.chk(i)**2)%self.MOD if i == j else (ans+self.chk(i)*self.chk(j)*2)%self.MOD
#         return ans
    
#     def numFactoredBinaryTrees(self, arr: List[int]) -> int:
#         self.MOD,self.arr = 10**9+7,sorted(arr)
        
#         return sum(self.chk(i) for i in range(len(arr)))

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod=10**9+7
        arr = sorted(arr)
        ans=defaultdict(int)
        for a in arr:
            tmp=1
            for b in arr:
                if b>a:
                    break
                tmp+=(ans[b]*ans[a/b])
            ans[a]=tmp
        return sum(ans.values())%mod            
        