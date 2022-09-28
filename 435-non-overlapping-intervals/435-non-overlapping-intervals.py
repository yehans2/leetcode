class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        PrevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= PrevEnd:
                PrevEnd = end
            else:
                res += 1
                PrevEnd = min(PrevEnd, end)
                
        return res
                