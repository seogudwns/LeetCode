class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        leng = len(needle)
        for i in range(len(haystack)-leng+1):
            if haystack[i:i+leng] == needle:
                return i
        
        return -1
        