class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr,comp = 0,0
        
        try:
            while True:
                if s[curr]==t[comp]: curr+=1
                comp+=1
        except:
            return curr == len(s) 
            