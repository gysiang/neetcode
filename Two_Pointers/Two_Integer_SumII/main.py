from typing import List
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		if not numbers:
			return []
		left = 0
		right = len(numbers)-1
		res = []
		while (right > left):
			currentsum = numbers[left] + numbers[right]
			if (currentsum < target):
				left += 1
			elif (currentsum > target):
				right -= 1
			else:
				res.append([left,right])
				left += 1
				right -= 1
		return (res)
