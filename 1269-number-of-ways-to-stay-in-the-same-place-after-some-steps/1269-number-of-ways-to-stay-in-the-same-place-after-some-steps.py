class Solution:
    @lru_cache(None)
    def chk(self,res,loc):
        if res == 0:
            return 1 if loc == 0 else 0
        if loc == 0: 
            return (self.chk(res-1,loc)+self.chk(res-1,loc+1))%self.MOD
        elif loc == self.arrLen:
            return (self.chk(res-1,loc-1)+self.chk(res-1,loc))%self.MOD
        else:
            return (self.chk(res-1,loc-1)+self.chk(res-1,loc)+self.chk(res-1,loc+1))%self.MOD

    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1: return 1
        self.MOD,self.arrLen = 10**9+7,min(steps//2+1,arrLen-1)
        return self.chk(steps,0)
        