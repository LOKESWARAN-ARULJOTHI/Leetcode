class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [i,dic[nums[i]]]
            else:
                dic[target-nums[i]]=i
            
            
# Algorithm - Dictionary
# Time - O(N)
# Space - O(N)
