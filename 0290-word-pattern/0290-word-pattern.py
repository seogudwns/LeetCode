class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if not len(pattern) == len(s):
            return False
        
        b = set()
        check = dict()
        for i in range(len(s)):
            if s[i] in b:
                if pattern[i] not in check or check[pattern[i]] !=s[i]:
                    return False
                continue
            if pattern[i] not in check:
                check[pattern[i]] = s[i]
                b.add(s[i])
            elif check[pattern[i]] != s[i]:
                return False
            
        return True