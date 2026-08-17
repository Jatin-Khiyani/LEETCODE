class Solution:
    def maxArea(self, heights: List[int]) -> int:

        index_left = 0 
        index_right = len(heights) - 1
        max_area = 0

        while index_left < index_right:

            max_area = max(
                            max_area,
                            ( (index_right-index_left) * min(heights[index_left],heights[index_right]) )
                        )
            
            if heights[index_left] < heights[index_right]:
                index_left += 1
            else:
                index_right -=1
        
        return max_area

