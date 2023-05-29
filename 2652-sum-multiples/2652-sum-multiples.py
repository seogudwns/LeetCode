class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(i if not (i%3 and i%5 and i%7) else 0 for i in range(n+1))