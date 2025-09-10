#Must run in O(n) time
#use set so that all the num is unique
#num_set = set(nums);
#loop through set to check for n-1, if n-1 exist, counter +1
from typing import List;

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		my_set = set(nums)
		longest = 0
		for num in my_set:
			if (num - 1) not in my_set:
				counter = 1
				current_num = num

				while ((current_num) + 1 in my_set):
					counter += 1
					current_num += 1

				longest = max(counter, longest)
		return (longest)

s = Solution()
s.longestConsecutive([0, -1])
