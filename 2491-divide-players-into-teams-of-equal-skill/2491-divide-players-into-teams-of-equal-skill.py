class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        l, r = 0, len(skill) - 1
        
        equal = skill[l] + skill[r]
        res = 0
        while l < r:
            if equal != skill[l] + skill[r]:
                return -1
            
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res
            
        
        