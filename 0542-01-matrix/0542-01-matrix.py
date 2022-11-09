class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    mat[i][j] = '#'
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = r + dr, c + dc
                    if (row < 0 or row >= len(mat) or col < 0 or col>= len(mat[0])) or mat[row][col] != '#':
                        continue
                    mat[row][col] = mat[r][c] + 1
                    q.append([row,col])
        
        return mat
                    
                    
            
                
                
        