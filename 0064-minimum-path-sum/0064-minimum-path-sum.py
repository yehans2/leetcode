class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i-1 < 0 and j-1 < 0:
                    grid[i][j] = grid[i][j]
                elif i-1 < 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j-1 < 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]