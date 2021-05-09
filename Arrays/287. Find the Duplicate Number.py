class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        hare=tortoise=0
        while True:
            tortoise=nums[tortoise]
            hare=nums[nums[hare]]
            if tortoise==hare:
                break
        tortoise=0
        while tortoise!=hare:
            tortoise=nums[tortoise]
            hare=nums[hare]
        return tortoise
            
        
        
        
# Algorithm - Floyd's Tortoise and hare algo(cycle detection)
# Time - O(N)
# Space - O(1)
