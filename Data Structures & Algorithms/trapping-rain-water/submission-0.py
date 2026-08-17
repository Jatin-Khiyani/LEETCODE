class Solution:
    def trap(self, height: List[int]) -> int:

        left_index = 0 

        right_index = len(height) - 1

        maxL = height[left_index]

        maxR = height[right_index]

        trapped_water = 0

        while left_index < right_index:

            if maxL <= maxR:

                left_index += 1
                maxL = max(maxL,height[left_index])
                trapped_water += maxL - height[left_index]
 

            else:

                right_index -=1
                maxR = max(maxR,height[right_index])
                trapped_water += maxR - height[right_index]

        return trapped_water

                




        