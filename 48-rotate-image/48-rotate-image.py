class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i, value in enumerate(zip(*matrix)):
            matrix[i] = value
      
        print(matrix)
       
    
            