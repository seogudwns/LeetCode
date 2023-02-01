class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str2),-1,-1):
            if i==0:
                return ""
            if not len(str1)%i and not len(str2)%i and str1==str2[:i]*(len(str1)//i) and str2==str2[:i]*(len(str2)//i): 
                return str2[:i]