class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        map={}
        for i in range(row):
            for j in range(col):
                key=i-j
                if key in map:
                    if map[key]!=matrix[i][j]:
                        return False
                else:
                    map[key]=matrix[i][j]
        return True
      
      
#Complexity:
# Time - O(m*n)
#Space - O(m+n)
