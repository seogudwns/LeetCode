class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        return sum(Counter(tuple(i) for i in grid)[tuple(grid[i][j] for i in range(len(grid)))] for j in range(len(grid)))    