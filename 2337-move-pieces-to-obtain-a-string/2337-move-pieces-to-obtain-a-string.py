class Solution:
    def canChange(self, start: str, target: str) -> bool:
                                                          
        if (len(start) != len(target) or 
            start.count('_') != target.count('_')): return False   

        s = [(ch,i) for i, ch in enumerate(start ) if ch != '_']
        t = [(ch,i) for i, ch in enumerate(target) if ch != '_']

        for i in range(len(s)):
            (sc, si), (tc,ti) = s[i], t[i]
            if sc != tc: return False                              
            if sc == 'L' and si < ti: return False                 
            if sc == 'R' and si > ti: return False                 

        return True                                                