class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i-1 not in s:
                length = 1
                cur = i
                while cur + 1 in s:
                    cur += 1
                    length += 1
                res = max(res, length)
        return res
        