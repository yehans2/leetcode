class Solution:
    def checkValidString(self, s: str) -> bool:
        left = right = 0
        
        for i in s:
            if i == '(':
                left += 1
                right += 1
            elif i == ')':
                left -= 1
                right -= 1
                if left < 0:
                    left = 0
                if right < 0:
                    return False
            if i == '*':
                left -= 1
                right += 1
                if left < 0:
                    left = 0
                if right < 0:
                    return False
        
        return left == 0 
    
 
   