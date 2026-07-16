class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final_area = 0
        left = 0
        right = len(heights)-1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            temp_area = width * height
            final_area = max(final_area, temp_area)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return final_area

        