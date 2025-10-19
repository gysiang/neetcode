from typing import List

class Solution:
	def maxArea(self, heights: List[int]) -> int:
		left = 0
		right = len(heights) - 1
		current_max = 0
		while (left < right):
			area = min(heights[left], heights[right]) * (right - left)
			if (area > current_max):
				current_max = area
			if (heights[left] < heights[right]):
				left += 1
			elif (heights[left] > heights[right]):
				right -= 1
			else:
				left += 1
				right -= 1
		return (current_max)
