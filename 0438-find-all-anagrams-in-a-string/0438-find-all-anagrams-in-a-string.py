class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # res = []
        # if len(p) > len(s):
        #     return []
        # for i in range(len(s)):
        #     if ''.join(sorted(s[i:i+len(p)])) == ''.join(sorted(p)):
        #         res.append(i)
        # return(res)
            
        
        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}
        
        for i in range(len(p)):
            pCount.setdefault(p[i], 0) 
            pCount[p[i]] += 1
            
            sCount.setdefault(s[i], 0)
            sCount[s[i]] += 1
        res = [0] if sCount == pCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount.setdefault(s[r], 0)
            sCount[s[r]] += 1
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res
      
        
            
        