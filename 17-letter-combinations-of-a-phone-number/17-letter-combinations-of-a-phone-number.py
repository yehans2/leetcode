class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num={'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}
        res=[]
        
        def dfs(i, letter):
            if i == len(digits):
                res.append(letter)
                return None
            
            for letters in num[digits[i]]:
                dfs(i + 1, letter + letters)
                
        dfs(0, '')
        return res
        