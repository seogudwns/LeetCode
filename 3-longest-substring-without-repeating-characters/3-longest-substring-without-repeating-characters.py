class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        seen = {}
        max_len = 0
        curr_max = 0
        l = 0
        r = 0
        while l < len(s):
            if s[r] not in seen:
                curr_max += 1
                seen[s[r]] = True
                r += 1
            else:
                if curr_max > max_len:
                    max_len = curr_max
                curr_max = 0
                l += 1
                r = l
                seen = {}
            if r >= len(s):
                break
        return max(curr_max, max_len)