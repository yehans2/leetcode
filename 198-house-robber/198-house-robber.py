class Solution:
    def rob(self, nums: List[int]) -> int:
        fir, sec = 0, 0
        for i in nums:
            Max = max(fir + i, sec)
            
            fir = sec
            sec = Max
        return Max