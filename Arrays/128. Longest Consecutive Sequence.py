class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        
        for num in nums:
            if num-1 not in nums:
                count=1
                start = num
                while start+1 in nums:
                    start += 1
                    count+=1
                res = max(res, count)
        return res
      
      
      
      
# DS - Set
# Time -O(N)
# Space - O(N)
