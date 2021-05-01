class Solution:
    def isMonotonic(self,A):
        length=len(A)
        val = None
        if length <= 2:
            return True
        if A[0]<=A[1]:
            for i in range(length-1):
                if A[i]<=A[i+1]:
                    val =True
                else:
                    val = False
                    break
        if A[0]>=A[1] and val != True:
            for i in range(length-1):
                if A[i]>=A[i+1]:
                    val =True
                else:
                    val = False
                    break
        return val

      
      
      
# Time - O(n)
# Space - O(1)
