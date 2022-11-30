class Solution:
    def searchMatrix(self, matrix, target):
        i = bisect_left(matrix, [target])
        print(i)
        print(len(matrix))
        if i < len(matrix) and matrix[i][0] == target:
            return True
        row = matrix[i-1]
        j = bisect.bisect_left(row, target)
        return j < len(row) and row[j] == target
