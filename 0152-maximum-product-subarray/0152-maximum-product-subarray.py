class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = 1, 1
        
        for n in nums:
            if n == 0:
                curr_max = 1
                curr_min = 1
            tmp = curr_max * n
            curr_max = max(tmp, n, n*curr_min)
            curr_min = min(tmp, n, curr_min * n)
            res = max(res, curr_max)
        return res
        

