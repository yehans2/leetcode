class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] *len(temperatures)
        stack = [] #[index tem]
        
        for  index, tem in enumerate(temperatures):
            while stack and tem > stack[-1][1]:
                stack_index, stack_tem = stack.pop()
                res[stack_index] = index - stack_index
            stack.append([index, tem])
        return res
        