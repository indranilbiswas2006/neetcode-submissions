class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,value in enumerate(nums): 
            hashmap[value] = index 
        
        if len(nums) == 2 and nums[0] + nums[1] == target: 
            return [0,1]

        for i, num in enumerate(nums):
            complement = target - num 

            if complement in hashmap and hashmap[complement] != i:
                return sorted([hashmap[complement], i])