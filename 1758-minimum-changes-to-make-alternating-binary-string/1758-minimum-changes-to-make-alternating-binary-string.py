class Solution:
    def minOperations(self, s: str) -> int:
        x = '01'*(len(s)//2)+'0'*(len(s)%2)
        return min(sum(1 if x[i] == s[i] else 0 for i in range(len(s))),sum(0 if x[i] == s[i] else 1 for i in range(len(s))))