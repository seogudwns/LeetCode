class Solution:
    def maxScore(self, nums: List[int]) -> int:
        Q,ans = [(nums,[])],0
        while Q:
            ns,res = Q.pop()
            if not ns:
                res = sorted(res)
                ans = max(ans,sum((i+1)*res[i] for i in range(len(res))))
                continue
            
            x = ns.pop()
            for i in range(len(ns)):
                Q.append((ns[:i]+ns[i+1:],res+[gcd(x,ns[i])]))
        
        return ans