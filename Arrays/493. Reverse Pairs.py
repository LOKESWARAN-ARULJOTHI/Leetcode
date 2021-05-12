class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        def merge(nums,start,end):
            if start>=end:
                return 0
            count=0
            mid=(start+end)//2
            
            count+=merge(nums,start,mid)
            count+=merge(nums,mid+1,end)
            
            left=start
            right=mid+1
            
            while left<=mid and right<=end:
                if nums[left]>2*nums[right]:
                    count+= mid-left+1
                    right+=1
                else:
                    left+=1
            
            nums[start:end+1]=sorted(nums[start:end+1])
            
            return count
        return merge(nums,0,len(nums)-1)
      

      
      
      
# Algorithm - Merge sort
# Time - O(N log N)
# Space - O(1)
