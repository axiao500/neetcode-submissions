class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if heights[left] <= heights[right]:
                left += 1
                current_area = min(heights[left], heights[right]) * (right - left)
                if current_area > max_area:
                    max_area = current_area
            if heights[left] > heights[right]:
                right -= 1
                current_area = min(heights[left], heights[right]) * (right - left)
                if current_area > max_area:
                    max_area = current_area
        return max_area



        