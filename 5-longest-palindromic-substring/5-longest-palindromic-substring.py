class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
         
        for i in range(len(s)):
            temp = self.check(s, i, i)
            if len(temp) > len(res):
                res = temp
                
        for i in range(len(s)):
            temp = self.check(s, i, i + 1)
            if len(temp) > len(res):
                res = temp
    
        return res   
    
    def check(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            r += 1
            l -= 1
        return s[1+l : r]