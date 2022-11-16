class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a_area = abs(ax1 - ax2) * abs(ay1 - ay2)
        b_area = abs(bx1 - bx2) * abs(by1 - by2)
        
   
        upper_right_x = min(ax2, bx2)
        upper_right_y = min(ay2, by2)

        bottom_left_x = max(ax1, bx1)
        bottom_left_y = max(ay1, by1)

        width = max(upper_right_x - bottom_left_x, 0)
        height = max(upper_right_y - bottom_left_y, 0)
        
        cover_area = width * height
        return a_area + b_area - cover_area