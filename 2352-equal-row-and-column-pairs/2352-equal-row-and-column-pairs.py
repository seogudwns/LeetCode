class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        X = Counter(tuple(i) for i in grid)
        return sum(X[tuple(grid[i][j] for i in range(len(grid)))] for j in range(len(grid)))    