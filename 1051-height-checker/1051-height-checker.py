class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        chk = sorted(heights)
        return sum(1 if chk[i] !=heights[i] else 0 for i in range(len(chk)))