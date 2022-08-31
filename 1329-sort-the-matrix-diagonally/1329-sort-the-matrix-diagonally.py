class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        
        row = len(mat)
        col = len(mat[0])
        
        for i in range(row):
            for j in range(col):
                if i - j not in hashmap:
                    hashmap[i-j] = [mat[i][j]]
                else:
                    hashmap[i-j].append(mat[i][j])
        
        for key in hashmap:
            hashmap[key].sort(reverse=True)
            
        for i in range(row):
            for j in range(col):
                mat[i][j] = hashmap[i-j][-1]
                hashmap[i-j].pop()
        
        return mat