class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n,unit = 0,1
        for i in num[::-1]:
            n+=unit*i
            unit*=10
        return [int(i) for i in str(n+k)]