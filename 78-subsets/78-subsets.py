class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        def recursive(index, subset):
            res.append(subset)
            for i in range(index, len(nums)):
                recursive(i + 1, subset + [nums[i]])
        recursive(0, [])
        return res
        