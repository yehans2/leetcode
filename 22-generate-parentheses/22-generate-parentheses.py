class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(l, r):
            if r == l == n:
                return res.append(''.join(stack))
            if l < n:
                stack.append("(")
                dfs(l + 1, r)
                stack.pop()
                
            if r < l:
                stack.append(")")
                dfs(l, r + 1)
                stack.pop()
        dfs(0, 0)
        return res
        