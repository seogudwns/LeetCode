class Solution:
    def countSubstrings(self, s: str) -> int:
        ans,leng = 0,len(s)
        for i in range(leng):
            l,r = i,i
            while True:
                if l < 0 or r == leng:
                    break
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break
            
            l,r = i,i+1
            while True:
                if l < 0 or r == leng:
                    break
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break
        return ans