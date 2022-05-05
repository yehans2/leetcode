class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                start = i - 1
                
                for j in range(len(nums) - 1, start, -1):
                    if nums[start] < nums[j]:
                        end = j
                        nums[start], nums[end] = nums[end], nums[start]
                        
                        for k in range((len(nums) - start) // 2):
                            nums[start + k + 1], nums[len(nums) - 1 - k] = nums[len(nums) -1 -k], nums[start + k + 1]
                        break
                        
                break
            if i == 1:
                nums.reverse()
        