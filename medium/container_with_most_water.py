class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            print("Left index:", left)
            print("Left height:", height[left])
            print("Right index:", right)
            print("Right height:", height[right])

            width = right - left
            print("Container width:", width)

            water_height = min(height[left], height[right])
            print("Usable water height:", water_height)

            area = width * water_height
            print("Container area:", area)

            max_area = max(max_area, area)
            print("Largest area so far:", max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            print("--------------------")

        return max_area


solution = Solution()
solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
