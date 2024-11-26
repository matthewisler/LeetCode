class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -1000
        left_side = 0
        right_side = len(height) - 1
        while left_side < right_side:
            current_area = min(height[left_side], height[right_side]) * (right_side - left_side)
            area = max(area, current_area)

            if height[left_side] < height[right_side]:
                left_side += 1
            else:
                right_side -= 1
        return area
        
