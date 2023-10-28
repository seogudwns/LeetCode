class Solution:
    @lru_cache(None)
    def chk(self,s,res):
        if res == 1: return 1
        return sum(self.chk(i,res-1) for i in self.resp[s])%self.MOD
    def countVowelPermutation(self, n: int) -> int:
        self.MOD = 10**9+7
        self.resp = {'a':['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
        return sum(self.chk(i,n) for i in['a','e','i','o','u'])%self.MOD