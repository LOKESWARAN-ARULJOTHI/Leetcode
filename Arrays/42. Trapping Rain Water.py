class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxleft=0
        maxright=0
        res=0
        
        while l<=r:
            if height[l]<=height[r]:
                if height[l]>maxleft: maxleft = height[l]
                else: res+= maxleft - height[l]
                l+=1
            else:
                if height[r]>maxright: maxright = height[r]
                else: res += maxright - height[r]
                r-=1
        
        return res
      
      
      
      
# Algorithm - Two pointer
# Time - O(N)
# Space - O(1)
