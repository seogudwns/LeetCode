class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = [1 if i in {'a','e','i','o','u'} else 0 for i in s]
        
        ans = curr = sum(s[:k])
        for i in range(k,len(s)):
            curr+=s[i]-s[i-k]
            ans = max(curr,ans)
        
        return ans
        