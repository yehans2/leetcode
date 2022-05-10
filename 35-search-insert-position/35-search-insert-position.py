class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r, l = len(nums)-1, 0
        while r >= l:
            m = (r+l) // 2
            if nums[m] < target:
                l += 1 
            elif nums[m] == target:
                return m
            else:
                r -= 1
        return l