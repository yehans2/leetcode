class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        for i in zip(*strs):
            word = ''.join(i)
            if len(set(word)) != 1:
                   return ans
            else:
                   ans+=word[0]
        return ans
            
            
                
            
        