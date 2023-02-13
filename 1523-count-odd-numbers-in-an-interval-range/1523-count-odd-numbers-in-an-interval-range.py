class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low)//2+1 if (high-low)%2 or low%2 else (high-low)//2