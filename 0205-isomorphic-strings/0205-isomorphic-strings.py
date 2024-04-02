class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        bimap1,bimap2 = dict(),dict()
        for i in range(len(s)):
            if s[i] not in bimap1:
                if t[i] in bimap2: return False
                else:
                    bimap1[s[i]] = t[i]
                    bimap2[t[i]] = s[i]
            else:
                if t[i] not in bimap2 or bimap2[t[i]] != s[i]: return False
        return True