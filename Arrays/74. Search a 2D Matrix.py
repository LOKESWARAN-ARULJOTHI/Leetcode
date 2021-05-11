class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high = (n*m)-1
        while low <= high:
            mid=(low+high)//2
            if matrix[mid//m][mid%m]==target:
                return True
            if matrix[mid//m][mid%m]>target:
                high=mid-1
            else:
                low=mid+1
        return False
      
      
      
# Algorithm - Binary search
# Time - O(log m*n)
# Space - O(1)
