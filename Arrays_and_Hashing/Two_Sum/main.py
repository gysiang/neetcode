from typing import List

class Solution:
    """
    Solves the Two Sum problem using a hash map.
    Time Complexity: O(n) as we iterate through the list once.
    Space Complexity: O(n) as in the worst case, we store all elements in the hash map.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # To store number -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_map:
                return [num_map[diff], i]
            num_map[n] = i

        # According to the problem description, a solution always exists.
        # However, it's good practice to handle the case where no solution is found.
        return []
