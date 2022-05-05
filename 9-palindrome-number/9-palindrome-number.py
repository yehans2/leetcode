class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=[i for i in str(x)]
        r, l = len(x) - 1, 0
        while r > l:
            if x[r] != x[l]:
                return False
            r -= 1
            l += 1
        return True
        