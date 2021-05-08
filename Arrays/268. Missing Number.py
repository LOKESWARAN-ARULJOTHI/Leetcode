class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums) #O(N)
        return expected_sum - actual_sum
      
      

#Algorithm : Guass formula - sum of array -len of array
# Time - O(N)
# Space - O(1)
