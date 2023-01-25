class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        if len(s) > 12:
            return res
        
        def  backtrack(i, dot, CurIp):
            if dot > 4:
                return
            if dot == 4 and i == len(s):
                res.append(CurIp[:-1])
                return
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'):
                    backtrack(j+1, dot+1, CurIp+s[i:j+1]+".")
        backtrack(0, 0, "")
        return res
        