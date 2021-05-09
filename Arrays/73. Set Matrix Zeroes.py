class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        stack = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    stack.append((row,col))
        
        while stack:
            r,c = stack.pop()
            for i in range(cols):
                if matrix[r][i] != 0:
                    matrix[r][i] = 0
            for j in range(rows):
                if matrix[j][c] != 0:
                    matrix[j][c] = 0
                    
                    
                    
                    
                    
# Time- O(M*N)
# Space - O(M+N)
