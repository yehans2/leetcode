class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        sum_num, max_num = nums[0], nums[0]
        for i in nums[1:]:
            sum_num = max(i, sum_num + i)
            max_num = max(sum_num, max_num)
            
        return max_num

        