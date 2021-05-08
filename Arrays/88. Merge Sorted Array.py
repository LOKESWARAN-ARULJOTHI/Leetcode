class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        writeindex=m+n-1
        while m>0 and n>0:
            if nums1[m-1]>=nums2[n-1]:
                nums1[writeindex]=nums1[m-1]
                m-=1
            else:
                nums1[writeindex]=nums2[n-1]
                n-=1
            writeindex-=1
        if n>0:
            nums1[:n]=nums2[:n]

            
            
            
            
# Time - O(N log N)
# Space - O(1)
