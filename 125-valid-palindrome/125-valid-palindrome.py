class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        l, r = 0, len(s)-1
        while r > l:
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True
        