class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        cnt = 0 
        for i in range(n):
            if nums[i] == 1: 
                cnt+= 1 
            elif nums[i] == 0: 
                res = max(cnt,res)
                cnt = 0
        res = max(cnt,res)
        return res