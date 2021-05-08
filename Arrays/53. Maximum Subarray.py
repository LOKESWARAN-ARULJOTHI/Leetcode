class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        add = 0
        maximum = nums[0]
        for num in nums:
            add+=num
            if add>maximum: maximum=add
            if add<0:add=0
        return maximum
      
      
      
# Algorithm = Kadane's Algorithm
# Time - O(N)
# Space - O(1)
