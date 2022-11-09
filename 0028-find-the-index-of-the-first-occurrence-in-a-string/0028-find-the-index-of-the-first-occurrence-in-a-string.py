class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        num = len(needle)
        for i in range(len(haystack)):
            if haystack[i:num+i] == needle:
                return i
        return -1
                
        