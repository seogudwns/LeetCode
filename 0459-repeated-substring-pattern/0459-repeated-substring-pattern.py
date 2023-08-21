class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return any(s[:i]*(len(s)//i)==s if not len(s)%i else False for i in range(1,len(s)//2+1))