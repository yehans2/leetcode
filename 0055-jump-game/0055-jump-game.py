class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [0] * len(nums) 
        
        dp[0] = nums[0]
        for i in range(1 , len(nums)):
            if dp[i-1] < i:
                return False
            
            dp[i] = max(dp[i-1], nums[i] + i)
            
            if dp[i] >= len(nums) - 1:
                return True
        