class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= [] 
        
        def dfs(i, combi, total):
            if total == target:
                res.append(combi.copy())
                return None
            if i >= len(candidates) or total > target:
                return None
            
            combi.append(candidates[i])
            dfs(i, combi, total + candidates[i])
            combi.pop()
            dfs(i+1, combi, total)
            # for j in candidates:
            #     combi.append(j)
            #     dfs(i+1, combi, total + j)
            #     combi.pop()
        dfs(0, [], 0)
        return res