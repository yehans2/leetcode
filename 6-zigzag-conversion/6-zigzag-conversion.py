class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        fig=[]
        for _ in range(numRows):
            fig.append('')
        
        mid = numRows - 1
        iters = mid * 2
        for i in range(len(s)):
            if i%iters < mid:
                fig[i%mid] += s[i]
            else:
                fig[mid - (i%mid)] += s[i]
                
        return ''.join(fig)
            