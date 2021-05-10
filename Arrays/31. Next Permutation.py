class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=j=len(a)-1
        while i>0 and a[i-1]>=a[i]:
            i-=1
        if i==0:
            a.reverse()
            return
        k=i-1
        while a[j]<=a[k]:
            j-=1
        a[j],a[k]=a[k],a[j]
        j=len(a)-1
        k+=1
        while j>k:
            a[j],a[k]=a[k],a[j]
            j-=1
            k+=1
            
            
            
            
            
# Algorithm: Single path approach
# Time - O(N)
# Space - O(1)
