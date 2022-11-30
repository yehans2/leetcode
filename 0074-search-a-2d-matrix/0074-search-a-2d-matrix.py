class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = bisect_left(matrix, target, key=lambda row: row[-1]) 
        print(r)
        return r < len(matrix) and matrix[r][bisect_left(matrix[r], target)] == target
# An alternative approach is to binary search across matrix in its entirety, as you would a 1D array.

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         n = len(matrix[0])
#         def get(idx: int) -> int:
#             r, c = divmod(idx, n)
#             return matrix[r][c]
#         return get(bisect_left(range(len(matrix)*n-1), target, key=get)) == target