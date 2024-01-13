class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s,t = Counter(s),Counter(t)
        return sum(abs(s[chr(i)]-t[chr(i)]) for i in range(97,126))//2