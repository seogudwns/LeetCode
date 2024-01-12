class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(Counter(s[:len(s)//2])[i] for i in ['a','e','i','o','u','A','E','I','O','U']) == sum(Counter(s[len(s)//2:])[i] for i in ['a','e','i','o','u','A','E','I','O','U'])