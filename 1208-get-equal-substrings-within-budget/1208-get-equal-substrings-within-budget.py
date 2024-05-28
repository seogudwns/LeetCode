class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        comp = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
        print(comp)
        l,r,val = 0,1,comp[0]
        ans = 0
        while True:
            # print(l,r,val,maxCost,val<=maxCost,r-l)
            if r<n:
                if val<=maxCost: 
                    ans = max(ans,r-l)
                    val += comp[r]
                    r += 1
                else:
                    val -= comp[l]
                    l += 1
            else:
                if val<=maxCost:
                    ans = max(ans,r-l)
                    break
                else:
                    val -= comp[l]
                    l += 1
        return ans
            
# "abcqeqweeewfrd"
# "brfdtgssfdscdf"
# 11
# "krpgjbjjznpzdfy"
# "nxargkbydxmsgby"
# 14