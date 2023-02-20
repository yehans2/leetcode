class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        r, l = len(nums) - 1, 0
        
        while r >= l:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return -1