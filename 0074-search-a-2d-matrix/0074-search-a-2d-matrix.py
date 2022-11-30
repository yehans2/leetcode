class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = sum(matrix, [])
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l+r)//2
            if matrix[m] == target:
                return True
            if matrix[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
                
            