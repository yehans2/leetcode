# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while True:
            m = (l + r) // 2
            if isBadVersion(m):
                if m == 1 or not isBadVersion(m-1):
                    return m
                r = m - 1
            else:
                l = m + 1
        