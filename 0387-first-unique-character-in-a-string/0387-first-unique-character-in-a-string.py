class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = min(s.index(i) if v == 1 else len(s)+1 for i,v in Counter(s).items())
        return ans if ans != len(s)+1 else -1
                