class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(0 if grid[i][j]>=0 else 1 for i in range(len(grid)) for j in range(len(grid[0])))
        # return sum([1 if grid[i] == sorted(grid[i],reverse=True) else 0 for i in range(len(grid))]
        #            + [1 if list(grid[j][i] for j in range(len(grid))) == sorted(list(grid[j][i] for j in range(len(grid))),reverse=True) else 0 for i in range(len(grid[0]))]
        #           )