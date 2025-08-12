class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def calc(n):
            ans,MOD = 1,10**9+7
            for i in range(n):
                ans *= 2
                ans %= MOD
            
            return ans

        tmp = bin(n)
        powers = []
        for i in range(2,len(tmp)):
            if tmp[i] == '1':
                powers.append(len(tmp)-i-1)
        
        powers = powers[::-1]
        
        return [calc(sum(powers[i:j+1])) for i,j in queries]