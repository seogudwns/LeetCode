class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return 0 if not left and not right else n-min(right) if not left else max(left) if not right else max(max(left),n-min(right))