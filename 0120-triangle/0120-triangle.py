MIN = 0.00001
def solver(row, col, triangle, cost):
    if row == len(triangle):
        return 0
    elif cost[row][col] == MIN:
        cost[row][col] = triangle[row][col] + min(solver(row+1, col, triangle, cost), solver(row+1, col+1, triangle, cost))
        
    return cost[row][col]
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        cost = [[MIN for i in range(len(triangle[j]))] for j in range(len(triangle))]
        return solver(0, 0, triangle, cost)
        