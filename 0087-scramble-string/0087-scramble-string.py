class Solution:
    def isScramble(self, s1: str, s2: str) -> int:
        @cache
        def chk(a:str, b:str) -> bool:
            if a==b: return True
            if Counter(a)!= Counter(b): return False
            return any((chk(a[:i],b[:i]) and chk(a[i:],b[i:])) or (chk(a[:i],b[-i:]) and chk(a[i:],b[:-i])) for i in range(1,len(a)))
        
        return chk(s1,s2)

## "abcde"    "caebd"
## "abb"    "bab"
## "abc"    