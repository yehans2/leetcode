class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        hashmap = dict()
        
        for index, value in enumerate(nums):
            if target - value in hashmap:
                return [index, hashmap[target - value]]
            else:
                hashmap[value] = index 
            
        