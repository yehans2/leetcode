class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        hashmap = {}
        for i, v in enumerate(s):
            if v in hashmap and l <= hashmap[v]:
                l = hashmap[v] + 1
            else:
                res = max(res, i - l + 1)
                
            hashmap[v] = i
        return res
            
            
            
        
        