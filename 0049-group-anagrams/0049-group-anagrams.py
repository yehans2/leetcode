class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort and save group
        table = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            table.setdefault(tmp,[])
            table[tmp].append(s)
        
        result = []
        # save result to list
        for i in table.values():
            result.append(i)
        return result
