class Solution:
    @lru_cache(None)
    def chk(self,curr,n):
        if n == 1: return 1
        return sum(self.chk(i,n-1) for i in self.dial[curr])%self.MOD

    
    def knightDialer(self, n: int) -> int:
        self.dial,self.MOD = {
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[3,9,0],
            5:[],
            6:[1,7,0],
            7:[2,6],
            8:[1,3],
            9:[2,4],
            0:[4,6]
        },10**9+7
        
        return sum(self.chk(i,n) for i in range(10))%self.MOD